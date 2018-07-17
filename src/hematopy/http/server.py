import os

import click
from sanic import Sanic

from ..log import logger
from ..donation.http_sanic import sanic_donation_bp_v1


file_dir = os.path.dirname(__file__)
img_dir = os.path.join(file_dir, 'images/')
assets_dir = os.path.join(file_dir, 'public/assets/')

if not os.path.exists(img_dir):
    os.makedirs(img_dir)

app = Sanic(__name__)
app.static('/images', img_dir)
app.blueprint(sanic_donation_bp_v1)


@click.group()
def cli_server():
    pass

@cli_server.command('serve')
@click.option('-h', '--host', type=(str), 
              help='Host name or IP \nDefault: 0.0.0.0')
@click.option('-p', '--port', type=(int), 
              help='Port to expose the service \nDefault: 8000')
@click.option('-d', '--debug', type=(bool), 
              help='Output debug messages \nDefault: True')
def cli_server_serve(host, port, debug=True):
    logger.info({'event': 'server_start'})
    
    _host = host if host != None else os.environ.get('HOST', '0.0.0.0')
    _port = port if port != None else os.environ.get('PORT', 8000)
    _debug = debug if debug != None else os.environ.get('DEBUG', True)
    
    app.run(host=_host, port=_port, debug=_debug)