import os

import click
from sanic import Sanic

from ..donation import sanic_donation_bp_v1


img_dir = os.path.join(os.path.dirname(__file__), 'images/')

if not os.path.exists(img_dir):
    os.makedirs(img_dir)

app = Sanic(__name__)
app.blueprint(sanic_donation_bp_v1)
app.static('/images', img_dir)


@click.group()
def cli():
    pass

@cli.command('serve')
def cli_serve():
    app.run(host=os.environ.get('HOST', '0.0.0.0'), 
            port=os.environ.get('PORT', 8000),
            debug=os.environ.get('DEBUG', True),)