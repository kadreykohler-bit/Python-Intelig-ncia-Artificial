from typing import List
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import engine, SessionLocal
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# 1. Configurações de Segurança
SECRET_KEY = "sua_chave_secreta_super_segura"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 2. Inicialização
models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="API Bancária Assíncrona")
templates = Jinja2Templates(directory="templates")


# 3. Dependências
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Funções Auxiliares de Segurança
def verificar_senha(senha_plana, senha_hashed):
    return pwd_context.verify(senha_plana, senha_hashed)


def gerar_hash_senha(senha):
    return pwd_context.hash(senha)


def criar_token_acesso(data: dict):
    copy_data = data.copy()
    expira = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    copy_data.update({"exp": expira})
    return jwt.encode(copy_data, SECRET_KEY, algorithm=ALGORITHM)


# --- ROTAS DE AUTENTICAÇÃO ---


@app.post("/usuarios/", response_model=schemas.UsuarioExibir)
async def cadastrar_usuario(
    usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)
):
    # 1. Busca se o usuário já existe
    db_user = (
        db.query(models.Usuario)
        .filter(models.Usuario.username == usuario.username)
        .first()
    )
    if db_user:
        raise HTTPException(status_code=400, detail="Usuário já cadastrado")

    # 2. Gera o hash da senha de forma segura
    try:
        senha_criptografada = gerar_hash_senha(usuario.password)
    except Exception as e:
        print(f"Erro na criptografia: {e}")
        raise HTTPException(
            status_code=500, detail="Erro ao processar segurança da senha"
        )

    # 3. Cria o objeto
    novo_usuario = models.Usuario(
        username=usuario.username, hashed_password=senha_criptografada
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario


@app.post("/token")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = (
        db.query(models.Usuario)
        .filter(models.Usuario.username == form_data.username)
        .first()
    )
    if not user or not verificar_senha(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Usuário ou senha incorretos")

    access_token = criar_token_acesso(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


# --- ROTAS DE NAVEGAÇÃO ---


@app.get("/")
async def raiz():
    return RedirectResponse(url="/financeiro")


@app.get("/financeiro", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    transacoes = db.query(models.Transacao).all()
    saldo = sum(t.valor if t.tipo == "receita" else -t.valor for t in transacoes)
    return templates.TemplateResponse(
        "index.html", {"request": request, "saldo": saldo, "transacoes": transacoes}
    )


# --- ROTAS DE API (PROTEGIDAS) ---


@app.post("/transacoes/", response_model=schemas.Transacao)
async def criar_transacao(
    transacao: schemas.TransacaoCreate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
):
    # Validação de Saldo (Requisito DIO)
    transacoes_existentes = db.query(models.Transacao).all()
    saldo_atual = sum(
        t.valor if t.tipo == "receita" else -t.valor for t in transacoes_existentes
    )

    if transacao.tipo == "despesa" and transacao.valor > saldo_atual:
        raise HTTPException(
            status_code=400, detail="Saldo insuficiente para esta operação"
        )

    nova_db_transacao = models.Transacao(**transacao.dict())
    db.add(nova_db_transacao)
    db.commit()
    db.refresh(nova_db_transacao)
    return nova_db_transacao


@app.get("/extrato/", response_model=List[schemas.Transacao])
async def consultar_extrato(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    return db.query(models.Transacao).all()
