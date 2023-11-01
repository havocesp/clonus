"""
'CLONUS'
partial github cloner
(C) 2023 hex benjamin (https://dev.hexbenjam.in)

adapted from 'HR/github-clone'
(C) 2019-2021 Habib Rehman (https://git.io/HR)

licensed under the APACHE-v2.0 license.
see './LICENSE' for more information.
"""

# sourcery skip: docstrings-for-modules

import os
import requests

from dotenv import load_dotenv
import click
from rich.console import Console

from clonus import __version__


def setup() -> None:
    """
    Set up the console and requests session.

    Returns:
        Tuple[Console, requests.Session]: A tuple containing the console and requests session objects.
    """

    load_dotenv()
    console = Console()
    req_session = requests.Session()
    req_session.headers.update({"User-Agent": f"hexbenjam.in/ {__version__}"})
    return console, req_session


def error(print_func: callable, message: str) -> None:
    """
    Print an error message and exit.

    Args:
        message (str): The error message to print.
    """

    print_func(f"[bold red]!!![/red] {message}")
    exit(1)


@click.command()
@click.option("-v", "--version", is_flag=True, help="print version and exit")
@click.argument("url")
@click.option(
    "-t", "--token", default=os.getenv("GITHUB_TOKEN"), help="github oauth token"
)
# @click.option("-p", "--path", default=".", help="path to clone to")
def clone(
    session: requests.Session,
    print_func: callable,
    version: bool,
    url: str = None,
    token: str = None,
) -> None:
    if version:
        print(__version__)
        exit(0)

    if not url:
        error(print_func, "no url specified.")

    if token:
        session.headers.update({"Authorization": f"token {token}"})


if __name__ == "__main__":
    _console, _reqsession = setup()
    _print = _console.print
    clone(_reqsession, _print)
