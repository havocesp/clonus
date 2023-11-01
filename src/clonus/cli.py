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

from dotenv import load_dotenv
import click

from clonus import __version__, CPRINT, SESSION, error, warn

from rich import inspect


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
        CPRINT(__version__)
        exit(0)

    if not url:
        error(CPRINT, "no url specified.")

    if token:
        SESSION.headers.update({"Authorization": f"Bearer {token}"})


if __name__ == "__main__":
    clone()
