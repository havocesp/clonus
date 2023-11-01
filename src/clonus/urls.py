"""
'CLONUS'
partial github cloner
(C) 2023 hex benjamin (https://dev.hexbenjam.in)

adapted from 'HR/github-clone'
(C) 2019-2021 Habib Rehman (https://git.io/HR)

licensed under the APACHE-v2.0 license.
see './LICENSE' for more information.
"""

import re

from clonus import error
from clonus.constants import BASE_NORMALIZE_REGEX, CONTENTS_ENDPOINT


def make_request(url: str) -> str:
    """
    Construct a GitHub API request URL from a GitHub URL.
    """
    normalized_url = re.sub(BASE_NORMALIZE_REGEX, "", url)
    api_args = normalized_url.replace("/tree", "").split("/")

    if len(api_args) < 2 or normalized_url == url:
        error("invalid GitHub URI.")

    user, repo = api_args[:2]
    rel_url = None

    if len(api_args) >= 2:
        # Clone entire repo
        path = repo

    ref = api_args[2] if len(api_args) >= 3 else None

    if len(api_args) >= 4:
        # Clone subdirectory
        rel_url = os.path.join(*api_args[3:])
        path = api_args[-1]

    return CONTENTS_ENDPOINT.format(user, repo)
