from fastapi import FastAPI
from router.router import actor

app = FastAPI()

app.include_router(actor)