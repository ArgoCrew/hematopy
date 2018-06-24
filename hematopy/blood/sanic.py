import os
import secrets

from sanic import Blueprint
from sanic.response import json

from ..banner.model import BannerBloodDonation
from ..http import server

IMG_HOST_BASE_URL = os.environ.get('IMG_HOST_BASE_URL', 'http://localhost:8000/images/')


blueprint_v1 = Blueprint('v1', url_prefix='/api/v1/donations')

@blueprint_v1.route('/', methods=['POST'])
async def create_donation_v1(request):
  def _parse_form_donate_action(request):
    donate_action = {}
    for key, value in request.form.items():
      donate_action[key] = value[0]

    donate_action['recipient_image'] = request.files['recipient_image'][0]

    return donate_action
  
  file_name = 'banner-blood-donation-{}.png'.format(secrets.token_urlsafe(10))
  file_dir = server.img_dir
  file_path = ''.join((file_dir, file_name))
  donate_action = _parse_form_donate_action(request)


  banner = BannerBloodDonation(donate_action=donate_action)
  banner.save(file_path)
  
  return json({'image': ''.join((IMG_HOST_BASE_URL, file_name))})