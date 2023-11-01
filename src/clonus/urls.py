"""
'CLONUS'
partial github cloner
(C) 2023 hex benjamin (https://dev.hexbenjam.in)

adapted from 'HR/github-clone'
(C) 2019-2021 Habib Rehman (https://git.io/HR)

licensed under the APACHE-v2.0 license.
see './LICENSE' for more information.
"""

import os
import re
from urllib.parse import urlparse, urljoin

from clonus import error


API_BASE_URL = "https://api.github.com"
TREE_ENDPOINT = "/repos/{owner}/{repo}/git/trees/{sha}/{subdir}"
BASE_NORMALIZE_REGEX = re.compile(r".*github\.com\/")


def make_request_url(url: str, owner: str, repo: str, branch: str, subdir: str) -> str:
    """
    Generate a request URL based on the provided parameters.

    Args:
        url (str): The original URL.
        owner (str): The owner (or username).
        repo (str): The repository name.
        branch (str): The branch or reference.
        subdir (str): The subdirectory, if applicable.

    Returns:
        str: The generated request URL.

    Raises:
        None.
    """

    parsed_url = urlparse(url)
    url_parts = parsed_url.path.strip("/").split("/")

    if "tree" in url_parts:
        url_parts.remove("tree")

    owner = owner or url_parts[0]
    repo = repo or url_parts[1]
    if not branch and len(url_parts) < 3:
        error("no branch specified by URL or argument.")
    else:
        branch = branch or url_parts[2]

    subdir = subdir or "/".join(url_parts[3:]) or ""

    return urljoin(
        API_BASE_URL,
        TREE_ENDPOINT.format(owner=owner, repo=repo, sha=branch, subdir=subdir),
    )


def resolve_path(path: os.PathLike, dir: os.PathLike) -> str:
    """
    Resolve a path by joining it with a root directory.

    Args:
        path (PathLike): The path to be resolved.
        dir (PathLike): The directory to be joined with the path.

    Returns:
        str: The resolved absolute path.

    Raises:
        None.
    """

    index = os.path.abspath
    if index == -1:
        return os.path.abspath(os.path.join(dir, path))
    else:
        return os.path.abspath(path[index:])
