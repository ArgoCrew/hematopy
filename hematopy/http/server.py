import os

import click
from sanic import Sanic

from ..donation.http_sanic import sanic_donation_bp_v1


file_dir = os.path.dirname(__file__)
img_dir = os.path.join(file_dir, 'images/')

if not os.path.exists(img_dir):
    os.makedirs(img_dir)

app = Sanic(__name__)
app.static('/', os.path.join(file_dir, 'public/index.html'))
app.static('/images', img_dir)
app.blueprint(sanic_donation_bp_v1)


@click.group()
def cli_server():
    pass

@cli_server.command('serve')
def cli_server_serve():
    app.run(host=os.environ.get('HOST', '0.0.0.0'), 
            port=os.environ.get('PORT', 8000),
            debug=os.environ.get('DEBUG', True),)