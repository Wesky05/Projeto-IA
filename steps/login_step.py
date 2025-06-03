# pylint: disable=missing-function-docstring,function-redefined
from behave import given, when, then  # pylint: disable=no-name-in-module
import requests

BASE_URL = "http://localhost:8000"

@given('o sistema está rodando')
def step_impl(context):
    context.session = requests.Session()

@when('eu envio usuário "{usuario}" e senha "{senha}" para login')
def step_impl(context, usuario, senha):
    payload = {
        "usuario": usuario,
        "senha": senha
    }
    response = context.session.post(f"{BASE_URL}/dashboard", data=payload, allow_redirects=False)
    context.response = response

@then('devo ser redirecionado para o dashboard')
def step_impl(context):
    assert context.response.status_code == 303, \
        f"Esperado 303, recebido {context.response.status_code}"

@then('devo receber uma mensagem de erro "{mensagem}"')
def step_impl(context, mensagem):
    response = context.response
    assert response.status_code == 200, "Esperava código 200 para página de erro"
    assert mensagem in response.text, f"Mensagem de erro não encontrada. Resposta: {response.text}"
