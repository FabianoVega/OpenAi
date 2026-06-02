from fastapi import APIRouter

estoque_route = APIRouter(prefix="/estoque", tags=["estoque"])

@estoque_route.get("/medicamentos")
async def get_medicamentos():
    """Endpoint para listar medicamentos em estoque"""
    return {"message": "Lista de medicamentos"}