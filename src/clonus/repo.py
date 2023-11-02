"""
'CLONUS.urls'
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

from urllib3 import PoolManager

from clonus import __version__, error


_headers = {
    "User-Agent": f"dev.hexbenjam.in/clonus {__version__}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

HTTP = PoolManager(headers=_headers)

API_BASE_URL = "https://api.github.com"
CONTENTS_ENDPOINT = "/repos/{owner}/{repo}/contents/{subdir}"
BASE_NORMALIZE_REGEX = re.compile(r".*github\.com\/")


class Repo:
    """
    Represents a repository.

    Args:
        url: The URL of the repository.
        token: The authentication token for accessing the repository.
        owner: The owner of the repository.
        repository: The name of the repository.
        ref: The reference (branch, tag, or commit) of the repository.
        subdir: The subdirectory within the repository.
        local_path: The local path where the repository will be cloned.

    Examples:
        >>> repo = Repo()
        >>> repo.owner = "octocat"
        >>> repo.repository = "Hello-World"
        >>> repo.subdir = "src"
        >>> repo.make_request_url()
        'https://api.github.com/repos/octocat/Hello-World/contents/src'
    """

    def __init__(
        self,
        url: str = None,
        token: str = None,
        owner: str = None,
        repository: str = None,
        ref: str = None,
        subdir: str = None,
        local_path: str = None,
    ):
        """
        Initialize the Repo object. Either the URL* OR the owner AND repository** must be passed at init.

        Args:
            url: The URL of the GitHub repository.*
            token: The access token for authentication.
            owner: The owner of the repository.**
            repository: The name of the repository.**
            ref: The branch, tag, or commit reference.
            subdir: The subdirectory to clone.
            local_path: The local path to clone the repository to.
        """

        self.token = token
        self.url = url
        self.owner = owner
        self.repository = repository

        if self.url:
            self.owner, self.repository = urlparse(self.url).path.split("/")[1:3]
        elif self.owner and self.repository:
            self.url = f"https://github.com/{self.owner}/{self.repository}"

        self.ref = ref
        self.local_path = local_path

        self.subdir = subdir
        self.params = f"?recursive=1&ref={self.ref}" if self.ref else "?recursive=1"

    def make_request_url(self) -> dict:
        """
        Generates the request URL for the repository contents.

        Returns:
            dict: The generated request URL.
        """

        return urljoin(
            API_BASE_URL,
            CONTENTS_ENDPOINT.format(
                owner=self.owner,
                repo=self.repository,
                subdir=self.subdir,
            ),
            self.params,
        )

    def request(self) -> dict:
        """
        Send a GET request to fetch metadata for the repository.

        Returns:
            dict: The JSON response containing the metadata.

        Raises:
            Exception: If the request fails or the response status is not successful.
        """

        response = HTTP.request("GET", self.make_request_url())
        return response.json()
