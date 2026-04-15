from fastapi import FastAPI
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)

app = FastAPI(title="GEN AI Demo API", version="1.0")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/demo")
def demo_endpoint():
    return {"message": "Demo API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
