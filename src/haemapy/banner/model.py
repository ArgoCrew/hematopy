import os.path
import base64
import mimetypes
import datetime

import lxml.etree as etree
import cairosvg

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

  def _validate_donate_action(self, data):
    assert isinstance(data, dict)
    return True

  def __init__(self, 
               template_name='request-for-blood-donation-facebook-v1',
               **kargs):
    template_path = self._make_template_path(template_name)
    assert os.path.exists(template_path)
    data = kargs['donate_action']
    assert self._validate_donate_action(data)
    
    self.template_path = template_path
    self.data = data 


  def save(self, fp, format='png', **params):
    d = self.data
    recipient_image = self.data['recipient_image']

    tree = etree.parse(self.template_path)

    image_mime_type = mimetypes.guess_type(recipient_image.name)
    image_base_64 = base64.b64encode(recipient_image.read()).decode('utf-8')
    el_image = tree.xpath(self.el_selectors['recipient_image'], namespaces=NSMAP)[0]
    el_image.attrib['{http://www.w3.org/1999/xlink}href'] = 'data:{};base64,{}'.format(image_mime_type[0], 
                                                                                       image_base_64)
    
    recipient_name_parts = d['recipient_name'].split()
    
    if len(recipient_name_parts) > 3:
      recipient_name_part_1 = ' '.join(recipient_name_parts[:3])
      recipient_name_part_2 = ' '.join(recipient_name_parts[3:])
    else:
      recipient_name_part_1, recipient_name_part_2 = name, ''
    
    el_r_name_part_1 = tree.xpath(self.el_selectors['recipient_name_part_1'], namespaces=NSMAP)[0]
    el_r_name_part_1.text = recipient_name_part_1.upper()
    
    el_r_name_part_2 = tree.xpath(self.el_selectors['recipient_name_part_2'], namespaces=NSMAP)[0]
    el_r_name_part_2.text = recipient_name_part_2.upper()
    
    el_r_blood_type = tree.xpath(self.el_selectors['recipient_image'], namespaces=NSMAP)[0]
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
    
    format = format.lower()

    fp = fp.format(datetime.datetime.utcnow())

    if format == 'png':
        return cairosvg.svg2png(bytestring=etree.tostring(tree), write_to=fp)
    if format == 'pdf':
        return cairosvg.svg2pdf(bytestring=etree.tostring(tree), write_to=fp)
    if format == 'ps':
        return cairosvg.svg2ps(bytestring=etree.tostring(tree), write_to=fp)
    if format == 'svg':
        return cairosvg.svg2svg(bytestring=etree.tostring(tree), write_to=fp)

    error_message = '''
"{}" is invalid file extension! The supported extension is "png". "pdf", "ps" and "svg".
'''
    raise ValueError(error_message.format(fp))