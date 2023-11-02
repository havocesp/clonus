"""
'CLONUS.cli'
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

from clonus import __version__, CPRINT, error
from clonus.repo import Repo

# from rich import inspect


@click.command()
@click.option("-v", "--version", is_flag=True, help="show version and exit")
@click.option("-U", "--url", default=None, help="github repository url")
@click.option(
    "-t",
    "--token",
    default=os.getenv("GH_TOKEN"),
    help="github oauth (classic) token. defaults to the 'GH_TOKEN' environment variable.",
)
@click.option("-O", "--owner", default=None, help="repository owner")
@click.option("-R", "--repo", default=None, help="repository name")
@click.option("--ref", default=None, help="ref [commit/branch/tag] name")
@click.option("--subdir", default=None, help="subdirectory of the repo to clone")
@click.option("-L", "--local-path", default=None, help="directory to clone into")
def clone(
    version: bool = False,
    url: str = None,
    token: str = None,
    owner: str = None,
    repo: str = None,
    ref: str = None,
    subdir: str = None,
    local_path: str = None,
) -> None:
    CPRINT("")
    CPRINT("welcome to [bold cornflower_blue]CLONUS[/]!\n+++\n")

    if version:
        CPRINT(f"v[bold cornflower_blue]{__version__}[/]")
        exit(0)

    load_dotenv()
    token = os.getenv("GH_TOKEN") or token

    if not url and not (owner and repo):
        error("no url specified.")

    if not local_path:
        local_path = os.path.join(os.getcwd(), "repos")

    repo_obj = Repo(url, token, owner, repo, ref, subdir, os.path.abspath(local_path))

    response = repo_obj.request()
    CPRINT(response)


if __name__ == "__main__":
    clone()
