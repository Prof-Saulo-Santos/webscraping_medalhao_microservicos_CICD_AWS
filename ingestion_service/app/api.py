from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from app.protocols import ScraperProtocol, RepositoryProtocol
from app.scraper import ArxivScraper
from app.repository import BronzeRepository

app = FastAPI(
    title="ArXiv Ingestion Service",
    description="Microserviço para coleta e armazenamento de dados do arXiv (Camada Bronze).",
    version="0.1.0", # Mantenha a versão do projeto sincronizada com o pyproject.toml. 
)                    # No momento do git, ao finalizar uma feature ou correção importante, execute o `make bump-minor`
                     # Esse comando ira incrementar a versão do projeto e atualizar os arquivos necessários.
                     


class IngestResponse(BaseModel):
    status: str
    message: str
    records_count: int


def get_scraper() -> ScraperProtocol:
    return ArxivScraper()


def get_repository() -> RepositoryProtocol:
    return BronzeRepository()


@app.post("/ingest", response_model=IngestResponse, status_code=201)
def ingest_arxiv_data(
    scraper: ScraperProtocol = Depends(get_scraper),
    repository: RepositoryProtocol = Depends(get_repository),
):
    """
    Endpoint síncrono para disparar a coleta de dados do arXiv.
    1. Realiza o scraping da página de busca definida na configuração.
    2. Salva os dados brutos em arquivo JSON na camada Bronze.
    """
    try:
        # 1. Scraping
        records = scraper.fetch()

        # 2. Persistência
        repository.save(records)

        return IngestResponse(
            status="success",
            message="Dados coletados e persistidos com sucesso.",
            records_count=len(records),
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro durante a ingestão: {str(e)}"
        )


@app.get("/health")
def health_check():
    return {"status": "ok"}
