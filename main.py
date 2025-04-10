from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Middleware para permitir requisições do navegador
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/receber-dados", response_class=HTMLResponse)
async def receber_dados(
    request: Request,
    nome: str = Form(...),
    cpf: str = Form(...),
    campo1: str = Form(None),
    campo2: str = Form(None),
    campo3: str = Form(None),
    campo4: str = Form(None)
):
    dados = {
        "nome": nome,
        "cpf": cpf,
        "campo1": campo1,
        "campo2": campo2,
        "campo3": campo3,
        "campo4": campo4,
    }
    return templates.TemplateResponse("dados.html", {"request": request, "dados": dados})
