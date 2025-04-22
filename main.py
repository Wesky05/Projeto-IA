from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import psycopg2
import numpy as np
import joblib
from fastapi.responses import RedirectResponse
from fastapi import status
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="chave-secreta-bem-segura")
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")
modelo = joblib.load("modelo_logistic_regression.joblib")

# Função para conectar ao banco PostgreSQL
def conectar_banco():
    conn = psycopg2.connect(
        host="easypanel.kwautomation.shop",
        port="30420",
        database="projeto_ia",
        user="KEVIN",
        password="kevin123",
        sslmode="disable"
    )
    return conn

# Tela de login inicial
@app.get("/", response_class=HTMLResponse)
async def tela_login(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Login do admin (se quiser implementar depois)
@app.get("/login-admin", response_class=HTMLResponse)
async def login_admin(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Formulário do paciente
@app.get("/formulario-paciente", response_class=HTMLResponse)
async def formulario_paciente(request: Request):
    return templates.TemplateResponse("formulário.html", {"request": request})

# Recebendo os dados do formulário
@app.post("/receber-dados", response_class=HTMLResponse)
async def receber_dados(
    request: Request,
    nome: str = Form(...),
    cpf: str = Form(...),
    genero: str = Form(...),
    histsuic: str = Form(...),
    histfam: str = Form(...),
    subuse: str = Form(...),
):
    # Mapeamento dos valores
    genero_val = 1 if genero.lower() == "masculino" else 0
    histsuic_val = 1 if histsuic.lower() == "sim" else 0
    histfam_val = 1 if histfam.lower() == "sim" else 0
    subuse_val = 1 if subuse.lower() == "sim" else 0

    # Fazer predição
    entrada = np.array([[genero_val, histsuic_val, histfam_val, subuse_val]])
    predicao = modelo.predict(entrada)[0]

    # Conectar ao banco PostgreSQL
    conn = conectar_banco()
    cursor = conn.cursor()
    query = """
        INSERT INTO requisicoes (nome, cpf, genero, suicidio_historico, familia_historico, substancias_uso, predicao)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nome, cpf, genero, histsuic, histfam, subuse, str(predicao)))
    conn.commit()
    cursor.close()
    conn.close()

    # Texto de retorno
    diagnostico = "Esquizofrenia" if predicao == 1 else "Não esquizofrenia"
    if diagnostico == "Esquizofrenia":
        mensagem = f"🛑 Atenção! O/A paciente {nome} apresenta risco de esquizofrenia. 🛑"
    else:
        mensagem = f"✅ O/A paciente {nome} não apresenta risco de esquizofrenia. ✅"

    # Passando a mensagem para o template
    return templates.TemplateResponse("formulário.html", {"request": request, "mensagem": mensagem})



@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    usuario = request.session.get("usuario", "Desconhecido")
    return templates.TemplateResponse("dashboard.html", {"request": request, "usuario": usuario})



# Simulando usuários para o exemplo
usuarios_validos = {
    "admin": "senha123"
}

@app.get("/login-admin")
def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/dashboard")
def login_admin(request: Request, usuario: str = Form(...), senha: str = Form(...)):
    # Verificar credenciais
    if usuario in usuarios_validos and usuarios_validos[usuario] == senha:
        # Redireciona para a rota do painel (Streamlit ou outra página)
        return RedirectResponse(url="https://dashboard.kwautomation.shop/", status_code=status.HTTP_303_SEE_OTHER)
    else:
        # Se as credenciais estiverem erradas, retornar para a página de login com erro
        return templates.TemplateResponse("login.html", {"request": request, "erro": "Usuário ou senha incorretos"})