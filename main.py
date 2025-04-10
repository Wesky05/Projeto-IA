from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Tela de login inicial
@app.get("/", response_class=HTMLResponse)
async def tela_login(request: Request):
    return templates.TemplateResponse("teladelogin.html", {"request": request})

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
    campo1: str = Form(...),
    campo2: str = Form(...),
    campo3: str = Form(...),
    campo4: str = Form(...)
):
    # Aqui você pode salvar no banco ou fazer o que quiser
    return templates.TemplateResponse(
        "formulário.html",{"request": request, "nome": nome})

@app.post("/login-admin", response_class=HTMLResponse)
async def login_admin(
    request: Request,
    usuario: str = Form(...),
    senha: str = Form(...)
):
    return templates.TemplateResponse("admin_dashboard.html", {
        "request": request,
        "usuario": usuario
    })
