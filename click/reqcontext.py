import click
import requests
import json


def load_network_config():
    return {
        "base_url": "https://jsonplaceholder.typicode.com",
        "timeout": 5
    }

@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj['network_config'] = load_network_config()

@cli.command()
@click.pass_context
def ping(ctx):
    config = ctx.obj['network_config']
    try:
        response = requests.get(config['base_url'], timeout=config['timeout'])
        if response.status_code == 200:
            click.echo("Server is reachable!")
        else:
            click.echo("Server returned an error!")
    except requests.RequestException as e:
        click.echo(f"Failed to reach server: {e}")

@cli.command()
@click.argument('endpoint')
@click.option("-f", "--file", type=click.File(mode='w'), required=False, default="output.json")
@click.pass_context
def get_data(ctx, endpoint, file):
    config = ctx.obj['network_config']
    url = f"{config['base_url']}/{endpoint}"
    try:
        response = requests.get(url, timeout=config['timeout'])
        if response.status_code == 200:
            json.dump(response.json(), file, indent=4)
            click.secho(f"Data from {endpoint} written to {file.name}", fg="green")
        else:
            click.secho(f"Failed to retrieve data: {response.status_code}", fg="red")
    except requests.RequestException as e:
        click.secho(f"Failed to reach endpoint {endpoint}: {e}", fg="red")

if __name__ == '__main__':
    cli()



# python3 reqcontext.py ping 
# python3 reqcontext.py get-data /posts/1 -f get_data.json