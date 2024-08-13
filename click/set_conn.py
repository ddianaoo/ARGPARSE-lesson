import click

@click.command()
@click.option("--username", "-u", envvar="NET_USER", prompt=True)
@click.option("--password", "-p", envvar="NET_PASSWORD", prompt=True, hide_input=True)
@click.option("--secret", "-s", envvar="NET_SECRET", prompt=True, hide_input=True)
def cli(username, password, secret):
    expected_password = "rewq4321"
    expected_secret = "q"
    if password == expected_password:
        if secret == expected_secret:
            click.secho(f'{username}: succesfully logged in', fg='green')
        else:
            click.secho(f'{username}: secret key isn`t correct', fg='red')    
    else:
        click.secho(f'{username}: error during authorization', fg='red')        
if __name__ == "__main__":
    cli()