from fastapi import FastAPI
from api.endpoints import pets
from core.data.database import init_tables
from core.data.db_initializer import init_entities

init_tables()
init_entities()
app = FastAPI()

app.include_router(pets.router)
