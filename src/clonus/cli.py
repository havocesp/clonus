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

from rich import inspect


def setup() -> None:
    """
    Set up the console and requests session.

    Returns:
        Tuple[Console, requests.Session]: A tuple containing the console and requests session objects.
    """

    load_dotenv()

    req_session = requests.Session()
    req_session.headers.update(
        {
            "User-Agent": f"dev.hexbenjam.in/clonus {__version__}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
    )
    return req_session


def error(print_func: callable, message: str) -> None:
    """
    Print a syled error message and exit.

    Args:
        message (str): The error message to print.
    """

    print_func(f"[bold red]!!![/red] {message}")
    exit(1)


@click.command()
@click.argument("url")
@click.option(
    "-v",
    "--version",
    is_flag=True,
    help="print version and exit",
)
@click.option(
    "-t",
    "--token",
    default=os.getenv("GH_TOKEN"),
    help="github oauth (classic) token",
)
# @click.option("-p", "--path", default=".", help="path to clone to")
def clone(
    version: bool,
    url: str = None,
    token: str = None,
) -> None:
    if version:
        _print(__version__)
        exit(0)

    if not url:
        error(_print, "no url specified.")

    if token:
        _reqsession.headers.update({"Authorization": f"Bearer {token}"})

    _print(url)


if __name__ == "__main__":
    _reqsession = setup()
    _print = Console().print
    clone()
