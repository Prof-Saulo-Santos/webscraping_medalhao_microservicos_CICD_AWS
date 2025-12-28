import json
from pathlib import Path
from datetime import datetime, timezone
from app.config import settings

class BronzeRepository:
    def __init__(self):
        self.base_path = Path(settings.BRONZE_DATA_PATH)

    def save(self, records: list[dict]) -> None:
        if not records:
            return

        self.base_path.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')
        filename = f"arxiv_{timestamp}.json"
        
        with open(self.base_path / filename, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)