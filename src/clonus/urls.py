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


CONTENTS_ENDPOINT = "https://api.github.com/repos/{}/{}/contents"
TREE_ENDPOINT = "/repos/{owner}/{repo}/git/trees/{sha}"
BASE_NORMALIZE_REGEX = re.compile(r".*github\.com\/")


def make_request_obj(url: str) -> None:
    """
    represents a URL object for making requests to a GitHub repository.
    """

    # https://github.com/hexbenjamin/clonus/tree/7068e8ebd5c971c8af769967bb09be9ef3d4dd1c/og/ghclone

    normalized_url = re.sub(BASE_NORMALIZE_REGEX, "", url)
    args = normalized_url.split("/")

    owner = args.pop(0)
    repo = args.pop(0)

    if "tree" in args:
        ref = args.pop(args.index("tree") + 1)
        args.pop(args.index("tree"))

    if args:
        rel_url = "/".join(args)


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
