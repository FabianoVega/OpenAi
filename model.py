from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# conexão do banco
db = create_engine("sqlite:///banco.db")

Base = declarative_base()