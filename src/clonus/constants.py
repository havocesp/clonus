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


API_BASE_URL = "https://api.github.com"
CONTENTS_ENDPOINT = API_BASE_URL + "/repos/{}/{}/contents"
BASE_NORMALIZE_REGEX = re.compile(r".*github\.com\/")
