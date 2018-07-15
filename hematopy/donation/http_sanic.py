import os
import secrets
from urllib.request import urlretrieve

from sanic import Blueprint
from sanic.response import json
from sanic import exceptions

from ..banner.model import BannerBloodDonation
from ..http import server

IMG_HOST_BASE_URL = os.environ.get('IMG_HOST_BASE_URL', 'http://localhost:8000/images/')
RECIPIENT_IMAGE_KEY = 'recipient_image'

sanic_donation_bp_v1 = Blueprint('v1', url_prefix='/api/v1/donations')

@sanic_donation_bp_v1.route('/', methods=['POST'])
async def donation_create_v1(request):
    def _parse_request_donate_action(request):
        headers = request.headers
        content_type = headers['content-type']
        
        tmp_img_path = '/tmp/tmp-image-{}.png'.format(secrets.token_urlsafe(10))

        if 'multipart/form-data' in content_type \
        or 'application/x-www-form-urlencoded' in content_type:
            donate_action = {}
            
            for key, value in request.form.items():
                donate_action[key] = value[0]

            with open(tmp_img_path, 'wb') as f:
                f.write(request.files[RECIPIENT_IMAGE_KEY][0].body)

            donate_action[RECIPIENT_IMAGE_KEY] = tmp_img_path
            return donate_action

        if 'application/json' in content_type:
            donate_action = request.json
            
            recipient_image_path, _ = urlretrieve(donate_action[RECIPIENT_IMAGE_KEY], 
                                                  tmp_img_path)
            
            donate_action[RECIPIENT_IMAGE_KEY] = recipient_image_path
            
            return donate_action

        exceptions.abort(406)
    
    file_dir = server.img_dir
    file_name = 'banner-blood-donation-{}.png'.format(secrets.token_urlsafe(10))
    file_path = ''.join((file_dir, file_name))
    donate_action = _parse_request_donate_action(request)

    banner = BannerBloodDonation(donate_action=donate_action)
    banner.save(file_path)

    os.remove(donate_action[RECIPIENT_IMAGE_KEY])

    return json({'image': ''.join((IMG_HOST_BASE_URL, file_name))})