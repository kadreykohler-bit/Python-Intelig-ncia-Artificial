from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

# --- SCHEMAS DE TRANSAÇÃO ---
class TransacaoCreate(BaseModel):
    valor: float
    descricao: str
    tipo: Literal["receita", "despesa"]

class Transacao(TransacaoCreate):
    id: int
    data: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

# --- SCHEMAS DE USUÁRIO ---
class UsuarioCreate(BaseModel):
    username: str
    password: str

class UsuarioExibir(BaseModel):
    id: int
    username: str

    model_config = ConfigDict(from_attributes=True)

