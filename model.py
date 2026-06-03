from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float, Boolean, Text
from sqlalchemy.orm import declarative_base

# conexão do banco
db = create_engine("sqlite:///banco.db")

Base = declarative_base()

# tabelas a serem criadas
#usuario
#medicamentos
#lote
#movimentações

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    senha = Column(String(100), nullable=False)
    admin = Column(Boolean, default=False)
    funcao = Column(String(100), nullable=False)
    ativo = Column(Boolean, default=True)