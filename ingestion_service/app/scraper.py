import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from app.config import settings

class ArxivScraper:
    def fetch(self) -> list[dict]:
        """
        Faz o fetch da página do arXiv e retorna uma lista de dicionários com os dados brutos.
        """
        try:
            response = requests.get(settings.ARXIV_BASE_URL, timeout=30)
            response.raise_for_status()
        except requests.RequestException as e:
            raise e

        soup = BeautifulSoup(response.text, "html.parser")
        records = []

        for item in soup.select("li.arxiv-result"):
            title = item.select_one("p.title")
            abstract = item.select_one("span.abstract-full")
            url = item.select_one("p.list-title a")

            if title and abstract and url:
                records.append({
                    "title": title.text.strip(),
                    "abstract": abstract.text.strip(),
                    "url": url["href"],
                    "collected_at": datetime.now(timezone.utc).isoformat(),
                })

        return records