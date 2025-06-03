import pandas as pd
from behave import given, when, then


@given('os dados de pacientes estão carregados no sistema')
def step_impl(context):
    context.df = pd.DataFrame({
        "Nome": ["Paciente A", "Paciente B", "Paciente C", "Paciente D", "Paciente E"],
        "CPF": ["00000000000", "11111111111", "22222222222", "33333333333", "44444444444"],
        "Gênero": ["Masculino", "Feminino", "Masculino", "Feminino", "Masculino"],
        "Histórico de Suicídio": ["Sim", "Não", "Sim", "Não", "Sim"],
        "Histórico Familiar": ["Sim", "Sim", "Não", "Não", "Sim"],
        "Substâncias de Uso": ["Sim", "Não", "Sim", "Não", "Sim"],
        "Predição": ["Sim", "Não", "Sim", "Não", "Sim"]
    })
    context.resultado = context.df.copy()


# ---------------- Filtros ----------------
@when('eu aplico o filtro de gênero "{genero}"')
def step_impl(context, genero):
    if genero != "Todos":
        context.resultado = context.df[context.df["Gênero"] == genero]
    else:
        context.resultado = context.df.copy()


@when('eu aplico o filtro de histórico de suicídio "{valor}"')
def step_impl(context, valor):
    if valor != "Todos":
        context.resultado = context.df[context.df["Histórico de Suicídio"] == valor]
    else:
        context.resultado = context.df.copy()


@when('eu aplico o filtro de histórico familiar "{valor}"')
def step_impl(context, valor):
    if valor != "Todos":
        context.resultado = context.df[context.df["Histórico Familiar"] == valor]
    else:
        context.resultado = context.df.copy()


@when('eu aplico o filtro de substâncias de uso "{valor}"')
def step_impl(context, valor):
    if valor != "Todos":
        context.resultado = context.df[context.df["Substâncias de Uso"] == valor]
    else:
        context.resultado = context.df.copy()


@when('eu aplico o filtro de predição "{valor}"')
def step_impl(context, valor):
    if valor != "Todos":
        context.resultado = context.df[context.df["Predição"] == valor]
    else:
        context.resultado = context.df.copy()


@when('eu busco pelo CPF válido')
def step_impl(context):
    context.resultado = context.df[context.df["CPF"] == "00000000000"]


@when('eu busco por um CPF inexistente')
def step_impl(context):
    context.resultado = context.df[context.df["CPF"] == "99999999999"]


# ---------------- Validação ----------------
@then('deve exibir apenas pacientes do gênero "{genero}"')
def step_impl(context, genero):
    assert all(context.resultado["Gênero"] == genero), \
        f"Existem pacientes fora do gênero {genero}"


@then('deve exibir apenas pacientes com histórico de suicídio "{valor}"')
def step_impl(context, valor):
    assert all(context.resultado["Histórico de Suicídio"] == valor), \
        f"Existem pacientes sem histórico de suicídio {valor}"


@then('deve exibir apenas pacientes com histórico familiar "{valor}"')
def step_impl(context, valor):
    assert all(context.resultado["Histórico Familiar"] == valor), \
        f"Existem pacientes sem histórico familiar {valor}"


@then('deve exibir apenas pacientes que usam substâncias "{valor}"')
def step_impl(context, valor):
    assert all(context.resultado["Substâncias de Uso"] == valor), \
        f"Existem pacientes sem substâncias de uso {valor}"


@then('deve exibir apenas pacientes com predição "{valor}"')
def step_impl(context, valor):
    assert all(context.resultado["Predição"] == valor), \
        f"Existem pacientes sem predição {valor}"


@then('deve exibir todos os pacientes, independente do {campo}')
def step_impl(context, campo):
    assert len(context.resultado) == len(context.df), \
        "Nem todos os pacientes foram exibidos"


@then('deve exibir apenas o paciente correspondente ao CPF informado')
def step_impl(context):
    assert len(context.resultado) == 1, "Não encontrou exatamente um paciente para o CPF informado"


@then('não deve exibir nenhum paciente')
def step_impl(context):
    assert context.resultado.empty, "Deveria não ter retornado nenhum paciente"

@then('deve exibir todos os pacientes, independente da predição')
def step_impl(context):
    assert len(context.resultado) == len(context.df), "Nem todos os pacientes foram exibidos"
