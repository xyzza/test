import click

from counter.server import run_app


@click.group()
def entry_point():
    pass


@click.command()
def runserver():
    click.echo("Starting server...")
    run_app()


entry_point.add_command(runserver)


if __name__ == "__main__":
    entry_point()
