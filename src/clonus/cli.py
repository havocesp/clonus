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

import click
from dotenv import load_dotenv

from clonus import __version__, CPRINT, HTTP, error
from clonus.urls import make_request_url

# from rich import inspect


@click.command()
@click.option("-v", "--version", is_flag=True, help="show version and exit")
@click.option("-u", "--url", default=None, help="github repository url")
@click.option(
    "-t",
    "--token",
    default=os.getenv("GH_TOKEN"),
    help="github oauth (classic) token",
)
@click.option("-o", "--owner", default=None, help="repository owner")
@click.option("-r", "--repo", default=None, help="repository name")
@click.option("-b", "--branch", default=None, help="branch name")
@click.option("-s", "--subdir", default=None, help="subdirectory of the repo to clone")
@click.option("-d", "--target-dir", default=os.getcwd(), help="directory to clone into")
def clone(
    version: bool = False,
    url: str = None,
    token: str = None,
    owner: str = None,
    repo: str = None,
    branch: str = None,
    subdir: str = None,
    target_dir: str = os.getcwd(),
) -> None:
    CPRINT("welcome to [bold cornflower_blue]CLONUS[/]!\n+++\n")

    if version:
        CPRINT(f"v[bold cornflower_blue]{__version__}[/]")
        exit(0)

    if not url:
        error("no url specified.")

    if token:
        HTTP.headers.update({"Authorization": f"Bearer {token}"})

    req_url = make_request_url(url, owner, repo, branch, subdir)
    target_dir = os.path.abspath(target_dir)

    CPRINT(f"final url: [bold cornflower_blue]{req_url}[/]")
    CPRINT(f"target dir: [bold medium_orchid]{target_dir}[/]")

    # Make the GET request


if __name__ == "__main__":
    clone()
