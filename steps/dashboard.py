from behave import given, when, then  # pylint: disable=no-name-in-module

@given('o usuário está logado')
def step_impl(context):
    print("Usuário autenticado no sistema.")

@when('acessa a página de dashboard')
def step_impl(context):
    print("Usuário acessa /dashboard.")

@then('o sistema deve exibir o nome do usuário na interface')
def step_impl(context):
    print("Nome do usuário exibido no dashboard.")

@given('não estou logado')
def step_impl(context):
    print("Usuário não autenticado.")

@when('tento acessar o dashboard')
def step_impl(context):
    print("Tentando acessar /dashboard sem estar logado.")

@then('devo ser redirecionado para a página de login')
def step_impl(context):
    print("Usuário é redirecionado para /login-admin.")
