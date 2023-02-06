from fastapi import APIRouter
from schema.actor_schema import ActorShema

actor = APIRouter()

@actor.get("/")
def root():
    return{"message": "primera version de CRUD"}

@actor.post("/api/actor")
def create_actor(data_actor: ActorShema):
  print(data_actor)