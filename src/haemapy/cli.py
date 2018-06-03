import base64
import mimetypes
import lxml.etree as etree
import click
import cairosvg

BANNE_TEMPLATE_PATH = './assets/request-for-blood-donation-facebook-v1.svg'
NSMAP = {
  'sodipodi': 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd',
  'cc': 'http://web.resource.org/cc/',
  'svg': 'http://www.w3.org/2000/svg',
  'dc': 'http://purl.org/dc/elements/1.1/',
  'xlink': 'http://www.w3.org/1999/xlink',
  'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
  'inkscape': 'http://www.inkscape.org/namespaces/inkscape'
}

@click.group()
def cli():
    pass

@cli.command()
@click.option('--image', prompt='Image of the person who need blood donation',
              type=click.File('rb'), help='Image of the person who need blood donation')
@click.option('--name', prompt='Name of Patient',
              help='The name of person who needs donation',
              default='JOSÉ MARIA PEREIRA SOUZA ARUDINO DO SANTOS')
@click.option('--blood-type', prompt='Blood Type of Patient',
              type=click.Choice(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']),
              default='AB+')
@click.option('--place-name', prompt='Name of place where the blood donation can be made',
              help='Name of place where the blood donation can be made',
              default='Hemoes')
@click.option('--address_street', prompt='Street address of place where the blood donation can be made',
              help='Street address of place where the blood donation can be made',
              default='Av. Mal. Campos, 1468')
@click.option('--address-number', prompt='Post Office Box Number of place where the blood donation can be made',
              help='Post Office Box Number of place where the blood donation can be made',
              default='1468')
@click.option('--address-district', prompt='Neighborhood or District of place where the blood donation can be made',
              help='Neighborhood or district of place where the blood donation can be made',
              default='Nazareth')
@click.option('--address-locality', prompt='City or Locality of place where the blood donation can be made',
              help='City or Locality of place where the blood donation can be made',
              default='Vitória')
@click.option('--address-region', prompt='State or Region of place where the blood donation can be made',
              help='State or Region of place where the blood donation can be made',
              default='ES')
@click.option('--address-postal-code', prompt='Postal Code of place where the blood donation can be made',
              help='State or Region of place where the blood donation can be made',
              default='29047-100')
def banner(image, name, blood_type, place_name, 
           address_street, address_number, 
           address_district, address_locality,
           address_region, address_postal_code):

    tree = etree.parse(BANNE_TEMPLATE_PATH)

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
    
    cairosvg.svg2png(bytestring=etree.tostring(tree), write_to='test.png')

if __name__ == '__main__':
    cli()