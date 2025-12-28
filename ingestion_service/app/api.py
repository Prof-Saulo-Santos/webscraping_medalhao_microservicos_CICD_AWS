from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.scraper import ArxivScraper
from app.repository import BronzeRepository

app = FastAPI(
    title="ArXiv Ingestion Service",
    description="Microserviço para coleta e armazenamento de dados do arXiv (Camada Bronze).",
    version="0.1.0"
)

class IngestResponse(BaseModel):
    status: str
    message: str
    records_count: int

@app.post("/ingest", response_model=IngestResponse, status_code=201)
def ingest_arxiv_data():
    try:
        scraper = ArxivScraper()
        records = scraper.fetch()
        
        repository = BronzeRepository()
        repository.save(records)
        
        return IngestResponse(
            status="success",
            message="Dados coletados e persistidos com sucesso.",
            records_count=len(records)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro durante a ingestão: {str(e)}")

@app.get("/health")
def health_check():
    return {"status": "ok"}