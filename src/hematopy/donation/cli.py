import datetime

import click

from ..banner.model import BannerBloodDonation


@click.group()
def cli_donation():
    pass

    
@cli_donation.group('create')
def cli_donation_create():
    pass


@cli_donation_create.command('donation')
@click.option('-ri', '--recipient-image', 
              prompt='Image of the person who need blood donation',
              help='Image of the person who need blood donation',
              type=click.Path(exists=True))
@click.option('-rn', '--recipient-name',
              prompt='Name of Patient',
              help='The name of person who needs donation',)
@click.option('-rbt', '--recipient-bloodtype',
              prompt='Blood Type of Patient',
              type=click.Choice(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']),)
@click.option('-ln', '--location-name', 
              prompt='Name of location where the blood donation can be made',
              help='Name of location where the blood donation can be made\nEx.: Hemoes',)
@click.option('-las', '--location-address-street', 
              prompt='Street address of place where the blood donation can be made',
              help='Street address of place where the blood donation can be made',)
@click.option('-lan', '--location-address-number', 
              prompt='Post Office Box Number of place where the blood donation can be made',
              help='Post Office Box Number of place where the blood donation can be made',)
@click.option('-lad', '--location-address-district', 
              prompt='Neighborhood or District of place where the blood donation can be made',
              help='Neighborhood or district of place where the blood donation can be made',)
@click.option('-lal', '--location-address-locality', 
              prompt='City or Locality of place where the blood donation can be made',
              help='City or Locality of place where the blood donation can be made',)
@click.option('-lar', '--location-address-region', 
              prompt='State or Region of place where the blood donation can be made',
              help='State or Region of place where the blood donation can be made',)
@click.option('-lapc', '--location-address-postal-code', 
              prompt='Postal Code of place where the blood donation can be made',
              help='State or Region of place where the blood donation can be made',)
@click.option('-o', '--output', 
              help='''Path and file name to output. Ex.:
                      gs://bucket-name/banner-name.png
                      ./bannername.png''',
              default='./hematopy-banner-blood-donation-{uid}.png')
def cli_donation_create(
    recipient_image, recipient_name, recipient_bloodtype, 
    location_name, location_address_street, location_address_number, 
    location_address_district, location_address_locality,
    location_address_region, location_address_postal_code,
    output):
  banner = BannerBloodDonation(donate_action=locals())
  banner.save(output)
