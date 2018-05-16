import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Name of Patient',
              help='The name of person who needs donation')
def banner(name):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo('Hello %s!' % name)

if __name__ == '__main__':
    cli()