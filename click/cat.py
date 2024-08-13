import click

@click.command()
@click.argument(
    "files",
    nargs=-1,
    type=click.File(mode="r"),
)
def cli(files):
    for file in files:
        click.secho(file.name.split('/')[-1], fg='green')
        click.echo(file.read().rstrip() + "\n")

if __name__ == "__main__":
    cli()
    

# python3 cat.py --help
# python3 cat.py file1.txt todolist.txt