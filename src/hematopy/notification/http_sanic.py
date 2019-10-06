from sanic import Blueprint
from sanic.response import json

from .factory import get_provider_sms


sanic_notification_bp_v1 = Blueprint('v1', url_prefix='/v1/notifications')

@sanic_notification_bp_v1.route('/', methods=['POST'])
async def notification_create_v1(request):
    provider_sms = get_provider_sms('aws')

    success, _id = provider_sms.send(
        request.form.get('phone_number'), 
        request.form.get('message')
    )

    if success:
        return json({'id': _id})
    else:
        return json(None, status=500)
