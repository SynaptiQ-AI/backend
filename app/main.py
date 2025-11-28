from fastapi import FastAPI
from app.routes.analysis import router as analysis_router
from app.routes.upload import router as upload_router

app = FastAPI(title="Synapti-Q Backend")

app.include_router(analysis_router, prefix="/analysis", tags=["Analysis"])
app.include_router(upload_router, prefix="/upload", tags=["Upload"])

@app.get("/")
def root():
    return {"status": "Synapti-Q Backend Running"}
