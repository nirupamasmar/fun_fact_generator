from fastapi import FastAPI
from routes.fact_router import router 

app = FastAPI()

app.include_router(router)