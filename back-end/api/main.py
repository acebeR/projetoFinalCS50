from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API do Projeto Angular")

# Modelos de dados
class Pergunta(BaseModel):
    id: int
    pergunta: str
    resposta: str

# "Banco de dados" fake em memória
perguntas_db = [
    {"id": 1, "pergunta": "Qual é a capital da França?", "resposta": "Paris"},
    {"id": 2, "pergunta": "Qual é 2+2?", "resposta": "4"}
]

# Rotas
@app.get("/")
def root():
    return {"message": "API funcionando!"}

@app.get("/perguntas", response_model=List[Pergunta])
def listar_perguntas():
    return perguntas_db

@app.get("/perguntas/{id}", response_model=Pergunta)
def buscar_pergunta(id: int):
    for p in perguntas_db:
        if p["id"] == id:
            return p
    return {"error": "Pergunta não encontrada"}

@app.post("/perguntas", response_model=Pergunta)
def criar_pergunta(pergunta: Pergunta):
    perguntas_db.append(pergunta.dict())
    return pergunta
