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

from clonus import error, HTTP


API_BASE_URL = "https://api.github.com"
CONTENTS_ENDPOINT = "/repos/{owner}/{repo}/contents/{subdir}"
BASE_NORMALIZE_REGEX = re.compile(r".*github\.com\/")


def make_request_url(
    url: str = None, owner: str = None, repo: str = None, subdir: str = None
) -> str:
    """
    Generate a request URL based on the provided parameters.

    Args:
        owner (str): The owner (or username).
        repo (str): The repository name.
        subdir (str): The subdirectory, if applicable.

    Returns:
        str: The generated request URL.

    Raises:
        None.
    """
    if url:
        owner, repo = urlparse(url).path.split("/")[1:3]
    return urljoin(
        API_BASE_URL,
        CONTENTS_ENDPOINT.format(owner=owner, repo=repo, subdir=subdir or ""),
    )


def make_request(owner, repo, subdir, req_url, params):
    response = HTTP.request("GET", req_url)
    try:
        response.raise_for_status()
    except Exception as e:
        error(f"failed to fetch metadata for '{owner}/{repo}' at '{subdir}'.")
    return response.json()


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
