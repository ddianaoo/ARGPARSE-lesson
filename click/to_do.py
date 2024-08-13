import click

PRIORITIES = {
    "o": "Optional",
    "l": "Low",
    "m": "Medium",
    "h": "High",
    "c": "Crucial"
}

@click.group()
def cli():
    pass

@cli.command()
@click.option("-f", "--file", type=click.Path(exists=False), required=True)
@click.option("-t", "--title", prompt="Enter the todo title", help="The title of the todo item.")
@click.option("-d", "--desc", prompt="Describe the todo", help="The description of the todo item.")
@click.option("-p", "--priority", type=click.Choice(PRIORITIES.keys()), prompt="Enter the priority", help="The priority of the todo item.")
def add(title, desc, priority, file):
    with open(file, "a+") as f:
        f.write(f"[Priority: {PRIORITIES[priority]}] {title}: {desc}\n")

@cli.command()
@click.argument("index", type=int, required=True)
@click.option("-f", "--file", type=click.Path(exists=True), required=True)
def delete(index, file):
    with open(file) as f:
        todo_list = f.read().splitlines()
    todo_list.pop(index)
    with open(file, 'w') as f:
        f.write("\n".join(todo_list) + "\n")

@cli.command()
@click.option("-p", "--priority", type=click.Choice(PRIORITIES.keys()), help="The priority of the todo item.")
@click.option("-f", "--file", type=click.Path(exists=True), required=True)
def list_todos(priority, file):
    with open(file) as f:
        todo_list = f.read().splitlines()
    if priority is None:
        for i, todo in enumerate(todo_list):
            print(f"({i}) - {todo}")
    else:
        for i, todo in enumerate(todo_list):
            if f"[Priority: {PRIORITIES[priority]}]" in todo:
                print(f"({i}) - {todo}")

if __name__ == '__main__':
    cli()
