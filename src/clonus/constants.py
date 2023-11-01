import re


GH_API_BASE_URL = "https://api.github.com"
GH_REPO_CONTENTS_ENDPOINT = GH_API_BASE_URL + "/repos/{}/{}/contents"
BASE_NORMALIZE_REGEX = re.compile(r".*github\.com\/")
