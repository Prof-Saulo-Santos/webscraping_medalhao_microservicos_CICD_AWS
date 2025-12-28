from typing import Protocol, List, Dict, Any

class ScraperProtocol(Protocol):
    def fetch(self) -> List[Dict[str, Any]]:
        """
        Contrato para classes de Scraper.
        Deve retornar uma lista de dicionários com os dados coletados.
        """
        ...

class RepositoryProtocol(Protocol):
    def save(self, records: List[Dict[str, Any]]) -> None:
        """
        Contrato para classes de Repositório.
        Deve receber uma lista de dicionários e persisti-los.
        """
        ...
