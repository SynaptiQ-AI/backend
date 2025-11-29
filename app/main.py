from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import your existing routers
from app.routes.analysis import router as analysis_router
from app.routes.upload import router as upload_router

# ------------------------------------------------
#  APP SETUP
# ------------------------------------------------
app = FastAPI(
    title="Synapti-Q Backend",
    description="Synapti-Q AI Backend API",
    version="1.0.0"
)

# ------------------------------------------------
#  CORS CONFIG (Required for Vercel Frontend)
# ------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "https://synapti-q.vercel.app",   # Your Vercel deployment
        "*",                              # Allow all (optional but convenient)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------
#  ROUTES
# ------------------------------------------------
app.include_router(analysis_router, prefix="/analysis", tags=["Analysis"])
app.include_router(upload_router, prefix="/upload", tags=["Upload"])


# ------------------------------------------------
# ROOT ENDPOINT
# ------------------------------------------------
@app.get("/")
def root():
    return {
        "status": "Synapti-Q Backend Running",
        "message": "API is live and connected"
    }


# ------------------------------------------------
# HEALTH CHECK ENDPOINT (Frontend Loader Uses This)
# ------------------------------------------------
@app.get("/api/health")
def health_check():
    """
    Returns 200 OK when backend is ready.
    Used by the frontend /loading screen.
    """
    return {"status": "ok", "backend": "healthy"}
