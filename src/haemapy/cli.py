import click

from .banner.cli import cli_root as banner_cli
from .http.server import cli as server_cli

haemapy_cli = click.CommandCollection(sources=[banner_cli, server_cli])

if __name__ == '__main__':
    haemapy_cli()