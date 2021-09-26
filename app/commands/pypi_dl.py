import re

import requests

DL_PATTERN = re.compile(r'downloads: \d*')
PYPI_DOWNLOAD_URL = (
    "https://img.shields.io/badge/dynamic/json?"
    "label=downloads&query=%24.total_downloads"
    "&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2FPincer"
)


async def pypi_dl_command():
    res = requests.get(PYPI_DOWNLOAD_URL)
    downloads = re.findall(DL_PATTERN, res.content.decode())[0]
    amount = downloads.split(' ')[1]
    return f"> `{amount}` *Updates every days*"
