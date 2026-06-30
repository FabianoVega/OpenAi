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

    def __init__(self, nome, email, senha, admin=False, funcao="", ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.admin = admin
        self.funcao = funcao
        self.ativo = ativo 

class Medicamento(Base):
    __tablename__ = "medicamentos"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=True)
    lote_id = Column(Integer, ForeignKey("lotes.id"), nullable=True)

    def __init__(self, nome, descricao="", lote_id=0):
        self.nome = nome
        self.descricao = descricao
        self.lote_id = lote_id

class Lote(Base):
    __tablename__ = "lotes"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    numero_lote = Column(String(100), nullable=False)
    data_validade = Column(DateTime, nullable=False)
    quantidade = Column(Integer, nullable=False)
    medicamento_id = Column(Integer, ForeignKey("medicamentos.id"), nullable=False)

    def __init__(self, numero_lote, data_validade, quantidade, medicamento_id):
        self.numero_lote = numero_lote
        self.data_validade = data_validade
        self.quantidade = quantidade
        self.medicamento_id = medicamento_id

class Movimentacao(Base):
    __tablename__ = "movimentacoes"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    medicamento_id = Column(Integer, ForeignKey("medicamentos.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    tipo_movimentacao = Column(String(50), nullable=False)  # Entrada ou Saída
    quantidade = Column(Integer, nullable=False)
    data_movimentacao = Column(DateTime, nullable=False)

    def __init__(self, medicamento_id, usuario_id, tipo_movimentacao, quantidade, data_movimentacao):
        self.medicamento_id = medicamento_id
        self.usuario_id = usuario_id
        self.tipo_movimentacao = tipo_movimentacao
        self.quantidade = quantidade
        self.data_movimentacao = data_movimentacao
