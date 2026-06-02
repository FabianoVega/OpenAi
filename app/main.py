
from fastapi import FastAPI
app = FastAPI()

from app.auth_routes import auth_router

from app.estoque_routes import estoque_route

app.include_router(auth_router)
app.include_router(estoque_route)





