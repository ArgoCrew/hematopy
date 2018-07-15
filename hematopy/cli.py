import click

from .donation.cli import cli_donation
from .http.server import cli_server

main = click.CommandCollection(sources=[cli_donation, cli_server])

if __name__ == '__main__':
    main()