#!/usr/bin/env python3
"""Example CLI module using click package."""


# Third party modules
import click


@click.group()
def cli() -> None:
    """Create a container to which other commands can be attached."""


@cli.command(help="Display Author Name")
@click.option("-verbose", "--verbose", is_flag=True, help="set the verbosity")
def author(verbose: str) -> None:
    """Returns details about the Author."""
    click.echo("Author name: Stephen R A King")
    if verbose:
        click.echo("Author eMail: stephen.ra.king@gmail.com")
