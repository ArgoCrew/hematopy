import click

from .banner.cli import cli_root as banner_cli

haemapy_cli = click.CommandCollection(sources=[banner_cli])

if __name__ == '__main__':
    haemapy_cli()