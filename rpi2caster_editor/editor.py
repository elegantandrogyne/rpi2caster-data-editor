# -*- coding: utf-8 -*-
"""Typeface and unit arrangement editor for rpi2caster development"""

from contextlib import suppress
import json
import click


@click.command()
@click.argument('src', type=click.File('r'), default='unit_arrangements.json')
@click.argument('out', type=click.File('w+'), default='unit_arrangements.json')
def arrangement(src, out):
    """Edit a unit-arrangement file"""
    source = json.load(src)
    print(source)
    result = source
    if click.confirm('Save?'):
        json.dump(result, out)


@click.command()
@click.argument('src', type=click.File('r'), default='typefaces.json')
@click.argument('out', type=click.File('w+'), default='typefaces.json')
def typeface(src, out):
    """Edit typeface info"""


@click.command()
@click.argument('src', type=click.File('r'))
@click.argument('out', type=click.File('w+'))
def main(src, out):
    """Choose what to do"""
    def finish(*_):
        """exit gracefully"""
        raise click.Abort

    options = {'a': arrangement, 't': typeface, 'x': finish}

    try:
        while True:
            click.echo(('Choose what to do:\n'
                        'a - edit unit arrangements,\n'
                        't - edit typefaces,\n',
                        'x - exit program'))
            option = click.getchar()
            with suppress(TypeError):
                options.get(option)(src, out)
    except click.Abort:
        click.echo('Finished.')
