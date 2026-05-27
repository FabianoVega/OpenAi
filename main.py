

from fastapi import FastAPI

app = FastAPI()


estoque = [
    {"id": 1, "nome": "Produto A", "quantidade": 10},
    {"id": 2, "nome": "Produto B", "quantidade": 5},
]


@app.get("/estoque")
def listar_estoque():
    return estoque
