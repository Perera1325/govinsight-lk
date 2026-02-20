from fastapi import FastAPI
from app.poverty.routes.poverty_routes import router as poverty_router

app = FastAPI(title="GovInsightLK API")

app.include_router(poverty_router, prefix="/poverty", tags=["Poverty"])


@app.get("/")
def root():
    return {"message": "GovInsightLK API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}