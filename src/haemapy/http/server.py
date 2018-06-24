import os

import click
from aiohttp import web
from PIL import Image

from ..banner.model import BannerBloodDonation


async def post_media_object(request):
    data = await request.post()
    recipient_image = data['recipient_image']
    print(dict(data))
    print(recipient_image.filename)

    banner_args = {
      'donate_action': data
    }
    banner = BannerBloodDonation(**dict(banner_args))
    banner.save('./test.png')

    return web.Response(text='its work')

app = web.Application()
app.add_routes([web.post('/media_objects', post_media_object)])

web.run_app(app, port=8081)


@click.group()
def cli():
    pass

@cli.command('serve')
def cli_serve():
  app.serve(os.environ.get('HOST', 'localhost'), 
            os.environ.get('PORT', 8000), 
            debug=True)