import os

import click


@click.group()
def cli():
    pass

@cli.command('serve')
def cli_serve():
    pass