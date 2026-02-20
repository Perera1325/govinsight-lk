from fastapi import FastAPI

app = FastAPI(title="GovInsightLK API")

@app.get("/")
def root():
    return {
        "message": "GovInsightLK API is running"
    }

@app.get("/health")
def health():
    return {"status": "ok"}