from behave import given, when, then  # pylint: disable=no-name-in-module
import joblib


@given('que eu tenho os dados {dados}')
def step_given_dados(context, dados):
    # Transforma string em lista de inteiros
    context.entrada = [int(x) for x in dados.strip('[]').split(',')]

@when('eu faço a predição com o modelo')
def step_quando_predicao(context):
    modelo = joblib.load("modelo_logistic_regression.joblib")
    resultado = modelo.predict([context.entrada])
    context.resultado = "Esquizofrenia" if resultado[0] == 1 else "Não esquizofrenia"

@then('o resultado deve ser "{esperado}"')
def step_entao_resultado(context, esperado):
    assert context.resultado == esperado