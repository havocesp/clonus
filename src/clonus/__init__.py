"""
'CLONUS'
partial github cloner
(C) 2023 hex benjamin (https://dev.hexbenjam.in)

adapted from 'HR/github-clone'
(C) 2019-2021 Habib Rehman (https://git.io/HR)

licensed under the APACHE-v2.0 license.
see './LICENSE' for more information.
"""

from rich.console import Console
from urllib3 import PoolManager


__version__ = "0.1.0"

_headers = {
    "User-Agent": f"dev.hexbenjam.in/clonus {__version__}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
HTTP = PoolManager(headers=_headers)

CPRINT = Console().print


def error(message: str) -> None:
    """
    Print a styled error message and exit.

    Args:
        message (str): The error message to print.
    """

    CPRINT(f"[bold red]!!![/] {message}")
    exit(1)


def warn(message: str) -> None:
    """
    Print a styled warning message.

    Args:
        message (str): The warning message to print.
    """

    CPRINT(f"[bold gold1][!][/] {message}")
