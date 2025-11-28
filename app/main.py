from fastapi import FastAPI
from app.routes.analysis import router as analysis_router
from app.routes.upload import router as upload_router
from app.routes.ai_engine import router as ai_router

app = FastAPI(
    title="Synapti-Q Backend",
    description="AI Biostatistics Processing Engine",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"status": "Synapti-Q Backend Running"}

# Register routers
app.include_router(analysis_router, prefix="/analysis", tags=["Analysis"])
app.include_router(upload_router, prefix="/upload", tags=["Upload"])
app.include_router(ai_router, prefix="/ai", tags=["AI Engine"])
