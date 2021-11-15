#!/usr/bin/env python3
import click

@click.command()
@click.argument('name')
@click.option('--count', '-c', default=1, help="number of times to greet")
def main(name, count):
    for i in range(count):
        print(f'Hello {name}!')
