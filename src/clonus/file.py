"""
'CLONUS.files'
partial github cloner
(C) 2023 hex benjamin (https://dev.hexbenjam.in)

adapted from 'HR/github-clone'
(C) 2019-2021 Habib Rehman (https://git.io/HR)

licensed under the APACHE-v2.0 license.
see './LICENSE' for more information.
"""

import os


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
