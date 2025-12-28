from unittest.mock import patch, MagicMock
from app.scraper import ArxivScraper

SAMPLE_HTML = """
<li class="arxiv-result">
    <p class="title">Machine Learning for Everyone</p>
    <span class="abstract-full">This is a test abstract.</span>
    <p class="list-title"><a href="https://arxiv.org/abs/1234.5678">arxiv:1234.5678</a></p>
</li>
"""

@patch("requests.get")
def test_scraper_fetch_success(mock_get):
    mock_response = MagicMock()
    mock_response.text = SAMPLE_HTML
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    scraper = ArxivScraper()
    results = scraper.fetch()

    assert len(results) == 1
    assert results[0]["title"] == "Machine Learning for Everyone"
    assert results[0]["url"] == "https://arxiv.org/abs/1234.5678"

@patch("requests.get")
def test_scraper_handle_empty_results(mock_get):
    mock_response = MagicMock()
    mock_response.text = "<html><body>No results</body></html>"
    mock_get.return_value = mock_response

    scraper = ArxivScraper()
    results = scraper.fetch()
    assert len(results) == 0