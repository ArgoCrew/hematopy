import os
import base64
from urllib.parse import urlparse

import lxml.etree as etree
import cairosvg
import magic
import uuid
from google.cloud import storage as storage_gc

from .. import storage
from ..log import logger

FILE_PATH = os.path.dirname(__file__)
NSMAP = {
    'sodipodi': 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd',
    'cc': 'http://web.resource.org/cc/',
    'svg': 'http://www.w3.org/2000/svg',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'xlink': 'http://www.w3.org/1999/xlink',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'inkscape': 'http://www.inkscape.org/namespaces/inkscape'
}


class BannerBloodDonation(object):
    """Donation Banner 

    Todo:
        * Move for donation.model package
    """

    templates_directory = os.path.join(FILE_PATH, './template')
    el_selectors = {
        'recipient_image': '//svg:image[@id="recipient_image"]',
        'recipient_name_part_1': '//svg:tspan[@id="recipient_name_part_1"]',
        'recipient_name_part_2': '//svg:tspan[@id="recipient_name_part_2"]',
        'recipient_blood_type': '//svg:tspan[@id="recipient_blood_type"]',
        'location_name': '//svg:tspan[@id="location_name"]',
        'location_address_part_1': '//svg:tspan[@id="location_address_part_1"]',
        'location_address_part_2': '//svg:tspan[@id="location_address_part_2"]',
    }

    def _make_template_path(self, filename, extension='svg'):
        return os.path.join(self.templates_directory,
                            '{}.{}'.format(filename, extension),)

    def __init__(self, 
                 template_name='request-for-blood-donation-facebook-v1',
                 **kargs):
        self.uid = uuid.uuid1()
        template_path = self._make_template_path(template_name)
        assert os.path.exists(template_path)
        data = kargs['donate_action']
        
        self.template_path = template_path
        self.data = data

    def save(self, uri_dest, **kargs):
        tree = etree.parse(self.template_path)
        d = self.data

        with open(d['recipient_image'], 'rb') as recipient_image:
            image_data = recipient_image.read()
            image_mime_type = magic.from_buffer(image_data, mime=True)
            image_base_64 = base64.b64encode(image_data)
            
        el_image = tree.xpath(self.el_selectors['recipient_image'], namespaces=NSMAP)[0]
        el_image.attrib['{http://www.w3.org/1999/xlink}href'] = 'data:{};base64,{}'.format(image_mime_type, 
                                                                                           image_base_64.decode('utf-8'))
        
        recipient_name_parts = d['recipient_name'].split()
        
        if len(recipient_name_parts) > 3:
            recipient_name_part_1 = ' '.join(recipient_name_parts[:3])
            recipient_name_part_2 = ' '.join(recipient_name_parts[3:])
        else:
            recipient_name_part_1, recipient_name_part_2 = ' '.join(recipient_name_parts), ''
        
        el_r_name_part_1 = tree.xpath(self.el_selectors['recipient_name_part_1'], namespaces=NSMAP)[0]
        el_r_name_part_1.text = recipient_name_part_1.upper()
        
        el_r_name_part_2 = tree.xpath(self.el_selectors['recipient_name_part_2'], namespaces=NSMAP)[0]
        el_r_name_part_2.text = recipient_name_part_2.upper()
        
        el_r_blood_type = tree.xpath(self.el_selectors['recipient_blood_type'], namespaces=NSMAP)[0]
        el_r_blood_type.text = self.data['recipient_blood_type'].upper()
        

        el_l_name = tree.xpath(self.el_selectors['location_name'], namespaces=NSMAP)[0]
        el_l_name.text = self.data['location_name'].upper()
        
        el_l_address_part_1= tree.xpath(self.el_selectors['location_address_part_1'],namespaces=NSMAP)[0]
        el_l_address_part_1.text = '{}, {}'.format(self.data['location_address_street'].upper(), 
                                                   self.data['location_address_number'].upper())
        el_l_address_part_2 = tree.xpath(self.el_selectors['location_address_part_2'],namespaces=NSMAP)[0]
        el_l_address_part_2.text = '{}, {} - {}, {}'.format(self.data['location_address_district'].upper(), 
                                                            self.data['location_address_locality'].upper(),
                                                            self.data['location_address_region'].upper(),
                                                            self.data['location_address_postal_code'].upper(),)
        
        uri = urlparse(uri_dest)
        file_format = uri.path.rpartition('.')[-1].lower()
        file_args = {
            'uid': self.uid,
            'format': file_format}

        if uri.scheme == 'gs':
            fp = '/tmp/hematopy-img-{uid}.{format}'.format(**file_args)
        else:
            fp = uri.path.format(**file_args)

        if file_format == 'png':
            cairosvg.svg2png(bytestring=etree.tostring(tree), write_to=fp)
        if file_format == 'pdf':
            cairosvg.svg2pdf(bytestring=etree.tostring(tree), write_to=fp)
        if file_format == 'ps':
            cairosvg.svg2ps(bytestring=etree.tostring(tree), write_to=fp)
        if file_format == 'svg':
            cairosvg.svg2svg(bytestring=etree.tostring(tree), write_to=fp)

        if uri.scheme == 'gs':
            client = storage.storage_gc.Client()
            file_path = uri.path.format(**file_args)

            with open(fp, 'rb') as file:
                object_stream = storage.GCSObjectStreamUpload(
                    client,
                    bucket_name=uri.netloc,
                    blob_name=file_path,)
                
                def file_read_chunked(file, chunk_size):
                    return iter(lambda: file.read(chunk_size), '')

                with open(fp, 'rb') as file:
                    with object_stream as obj_stream:
                        file_chunks = file_read_chunked(file, 
                                                        obj_stream._chunk_size)
                        for data in file_chunks:
                            obj_stream.write(data)
                            if data == b'':
                                break;

            os.remove(fp)

        _d = d.copy()
        (_d.pop(k) for k in 'recipient_name recipient_image'.split())
        logger.info({
            'type': 'banner_generated',
            'data': {
                'donation': _d,
                '_meta': {
                    'file_format': file_format,
                }
            },
        })
        return True, 

        error_message = '''
"{}" is invalid file extension! The supported extension is "png". "pdf", "ps" and "svg".
'''
        raise ValueError(error_message.format(fp))
