from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.analysis import router as analysis_router
from app.routes.upload import router as upload_router

app = FastAPI(title="Synapti-Q Backend")

# ✅ CORS CONFIG (Important for Vercel Frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "https://synapti-q.vercel.app",  # Replace with your real Vercel domain later
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analysis_router, prefix="/analysis", tags=["Analysis"])
app.include_router(upload_router, prefix="/upload", tags=["Upload"])

@app.get("/")
def root():
    return {
        "status": "Synapti-Q Backend Running",
        "message": "API is live and connected"
    }
