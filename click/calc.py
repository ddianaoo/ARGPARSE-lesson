import click
from functools import reduce


operations = {
    "add": lambda x: sum(x),
    "mult": lambda x: reduce(lambda a,b: a*b, x, 1),
}


@click.command()
@click.option("-op", "--operation", type=click.Choice(operations.keys()), required=True)
@click.argument("intlist", nargs=-1, required=True, type=click.INT)
def cli(intlist, operation):
    click.echo(operations[operation](intlist))


if __name__ == "__main__":
    cli()

# python3 calc.py --help
# python3 calc.py --operation add 10 20 30
# python3 calc.py --operation mult 10 20
# python3 calc.py --operation a 10 20