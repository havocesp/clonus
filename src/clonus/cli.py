# sourcery skip: docstrings-for-modules
# import requests
import click

# from clonus import __version__


# REQ = requests.Session()
# REQ.headers.update({"User-Agent": f"hexbenjam.in/ {__version__}"})


@click.command()
def hello() -> None:
    """
    Say "wello" to the "Horld".
    """
    click.echo("wello, Horld!")


if __name__ == "__main__":
    hello()
