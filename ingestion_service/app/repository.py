import json
from pathlib import Path
from datetime import datetime, timezone
from app.config import settings
from app.protocols import RepositoryProtocol


class BronzeRepository(RepositoryProtocol):
    def __init__(self):
        self.base_path = Path(settings.BRONZE_DATA_PATH)

    def save(self, records: list[dict]) -> None:
        """
        Salva os registros em um arquivo JSON na camada Bronze.
        O nome do arquivo é gerado com base no timestamp atual (UTC).
        """
        if not records:
            return

        self.base_path.mkdir(parents=True, exist_ok=True)

        # Gera nome do arquivo: arxiv_YYYYMMDDHHMMSS.json
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        filename = f"arxiv_{timestamp}.json"
        file_path = self.base_path / filename

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
