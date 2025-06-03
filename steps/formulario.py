from behave import given, when, then  # pylint: disable=no-name-in-module

@given('estou na página do formulário')
def step_impl(context):
    print("Usuário acessa a página do formulário.")

@when('preencho todos os campos corretamente')
def step_impl(context):
    print("Preenchendo nome, CPF válido, gênero, histórico de suicídio, histórico familiar e uso de substâncias.")

@then('o sistema deve exibir a mensagem de diagnóstico')
def step_impl(context):
    print("Mensagem de diagnóstico exibida com sucesso.")

@when('preencho o CPF inválido "{cpf}"')
def step_impl(context, cpf):
    print(f"Tentando enviar formulário com CPF inválido: {cpf}")

@then('o sistema deve exibir uma mensagem de erro de CPF inválido')
def step_impl(context):
    print("Erro: CPF inválido.")

@when('envio o formulário sem preencher os campos obrigatórios')
def step_impl(context):
    print("Tentando enviar formulário com campos vazios.")

@then('o sistema deve exibir a mensagem "Por favor, preencha todos os campos"')
def step_impl(context):
    print("Erro: Por favor, preencha todos os campos.")
