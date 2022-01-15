import click
import openasis.core.core as cr

@click.command()
@click.option(
 '--command',
 '-c',
 help='Command that will be queried')

def main(command):
    click.echo(cr.take_query(command))
