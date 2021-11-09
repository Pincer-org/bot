from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class PyPI:
    total_downloads: Optional[int] = None
    downloads: Optional[Dict[str, int]] = None
    daily_average: Optional[float] = None
    daily_max: Optional[int] = None

    def update(self, json):
        self.total_downloads = json.get('total_downloads')
        self.downloads = json.get('downloads')

        self.daily_average = sum(self.downloads.values()) / len(self.downloads)
        self.daily_max = max(self.downloads.values())
