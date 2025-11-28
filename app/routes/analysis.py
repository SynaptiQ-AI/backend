from fastapi import APIRouter
from app.services.biostat_engine import run_analysis


router = APIRouter()


@router.post("/")
def analyze(data: dict):
result = run_analysis(data)
return {"result": result}