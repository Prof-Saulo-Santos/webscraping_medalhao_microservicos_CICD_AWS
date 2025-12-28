import json
from app.repository import BronzeRepository

def test_repository_save_creates_file(tmp_path):
    repo = BronzeRepository()
    repo.base_path = tmp_path

    data = [{"title": "Test Paper", "url": "http://arxiv.org/1"}]
    repo.save(data)

    files = list(tmp_path.glob("*.json"))
    assert len(files) == 1
    
    with open(files[0], "r", encoding="utf-8") as f:
        saved_data = json.load(f)
    assert saved_data == data

def test_repository_save_does_nothing_if_empty(tmp_path):
    repo = BronzeRepository()
    repo.base_path = tmp_path
    repo.save([])
    assert len(list(tmp_path.glob("*.json"))) == 0