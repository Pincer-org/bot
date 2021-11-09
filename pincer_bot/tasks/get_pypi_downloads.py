from __future__ import annotations

import requests
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pincer_bot.bot import Bot

API_LINK: str = "https://api.pepy.tech/api/projects/Pincer"


async def get_pypi_stats(self: Bot):
    response = requests.get(API_LINK)
    self.pypi.update(response.json())
