from fastapi import APIRouter
from models.topic_schema import topic_schema
from services.fun_fact_generator import generate_llm_response

router = APIRouter()

@router.post("/generate")
async def generate_fun_fact(request:topic_schema):
    fun_fact = generate_llm_response(request.topic)
    return {"fun_fact": fun_fact}
