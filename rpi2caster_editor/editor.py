# -*- coding: utf-8 -*-
"""Typeface and unit arrangement editor for rpi2caster development"""

import json
import click


@click.command()
@click.argument('src', type=click.File('r'), default='unit_arrangements.json')
@click.argument('out', type=click.File('w+'), default='unit_arrangements.json')
def arrangement(src, out):
    """Edit a unit-arrangement file"""
    with open(src) as jsonfile:
        source = json.load(jsonfile)
    print(source)
    result = source
    if click.confirm('Save?'):
        with open(out) as jsonfile:
            json.dump(result, jsonfile)


@click.command()
@click.argument('src', type=click.File('r'), default='typefaces.json')
@click.argument('out', type=click.File('w+'), default='typefaces.json')
def typeface(src, out):
    """Edit typeface info"""
