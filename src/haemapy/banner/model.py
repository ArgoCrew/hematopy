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

  templates_directory = os.path.join(FILE_PATH, '../../../assets')

  def _make_template_path(self, filename, extension='svg'):
    return os.path.join(self.templates_directory,
                        '{}.{}'.format(filename, extension),)

  def _validate_donate_action(self, donate_action):
    assert isinstance(donate_action, dict)
    return True

  def __init__(self, 
               template_name='request-for-blood-donation-facebook-v1',
               **kargs):
    template_path = self._make_template_path(template_name)
    assert os.path.exists(template_path)
    donate_action = kargs['donate_action']
    assert self._validate_donate_action(donate_action)
    
    self.template_path = template_path
    self.donate_action = donate_action 


  def save(self, fp, format='png', **params):
    image = self.donate_action['recipient_image']
    name = self.donate_action['recipient_name']
    blood_type = self.donate_action['recipient_blood_type']
    place_name = self.donate_action['location_name']
    address_street = self.donate_action['location_address_street']
    address_number = self.donate_action['location_address_number']
    address_district = self.donate_action['location_address_district']
    address_locality = self.donate_action['location_address_locality']
    address_region = self.donate_action['location_address_region']
    address_postal_code = self.donate_action['location_address_postal_code']

    tree = etree.parse(self.template_path)

    image_mime_type = mimetypes.guess_type(image.name)
    image_base_64 = base64.b64encode(image.read()).decode('utf-8')
    e_image = tree.xpath('//svg:image[@id="image"]',namespaces=NSMAP)[0]
    
    e_image.attrib['{http://www.w3.org/1999/xlink}href'] = 'data:{};base64,{}'.format(image_mime_type[0], image_base_64)
    
    name_parts = name.split()
    
    if len(name_parts) > 3:
      name_l1 = ' '.join(name_parts[:3])
      name_l2 = ' '.join(name_parts[3:])
    else:
      name_l1 = name
      name_l2 = ''
    
    e_name_l1 = tree.xpath('//svg:tspan[@id="name_l1"]',namespaces=NSMAP)[0]
    e_name_l1.text = name_l1.upper()
    e_name_l2 = tree.xpath('//svg:tspan[@id="name_l2"]',namespaces=NSMAP)[0]
    e_name_l2.text = name_l2.upper()
    
    e_blood_type = tree.xpath('//svg:tspan[@id="blood_type"]',namespaces=NSMAP)[0]
    e_blood_type.text = blood_type.upper()
    e_place_name = tree.xpath('//svg:tspan[@id="place_name"]',namespaces=NSMAP)[0]
    e_place_name.text = place_name.upper()
    
    e_address_l1 = tree.xpath('//svg:tspan[@id="address_l1"]',namespaces=NSMAP)[0]
    e_address_l1.text = '{}, {}'.format(address_street.upper(), 
                                        address_number.upper())
    e_address_l2 = tree.xpath('//svg:tspan[@id="address_l2"]',namespaces=NSMAP)[0]
    e_address_l2.text = '{}, {} - {}, {}'.format(address_district.upper(), 
                                             address_locality.upper(),
                                             address_region.upper(),
                                             address_postal_code.upper())
    
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