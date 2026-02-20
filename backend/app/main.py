from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.poverty.routes.poverty_routes import router as poverty_router

app = FastAPI(title="GovInsightLK API")

# ✅ CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(poverty_router, prefix="/poverty", tags=["Poverty"])


@app.get("/")
def root():
    return {"message": "GovInsightLK API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}