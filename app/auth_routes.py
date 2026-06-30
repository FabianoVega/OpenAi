from fastapi import APIRouter, Depends
from app.dependences import pegar_sessao
from database.model import Usuario,db
from app.dependences import pegar_sessao

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():

    """Rota home para autenticação"""
    return {"message": "autenticação bem sucedida"}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, funcao: str, session = Depends(pegar_sessao)):
    """Rota para criar uma nova conta de usuário"""
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario: #quer dizer que o email já existe
        return {"message": "Email já cadastrado"}
    else:
        novo_usuario = Usuario(email=email, senha=senha, nome=nome, funcao=funcao)
        session.add(novo_usuario)
        session.commit()
    return {"message": f"Conta criada com sucesso para o email: {email}"}




# @auth_router.post("/criar_conta")
# async def criar_conta(email: str, senha: str):
#     """Rota para criar uma nova conta de usuário"""
#     Session = sessionmaker(bind=db)
#     session = Session()
#     usuario = session.query(Usuario).filter(Usuario.email == email).first()
#     if usuario: #quer dizer que o email já existe
#         return {"message": "Email já cadastrado"}
#     else:
#         novo_usuario = Usuario(email=email, senha=senha)
#         session.add(novo_usuario)
#         session.commit()
#         session.refresh(novo_usuario)
#     return {"message": f"Conta criada com sucesso para o email: {email}"}

