from pydantic import BaseModel

class AnalysisRequest(BaseModel):
    data: dict

class AnalysisResponse(BaseModel):
    result: dict
