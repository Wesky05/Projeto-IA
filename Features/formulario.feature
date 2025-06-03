Feature: Envio do Formulário de Paciente

  Scenario: Enviar formulário com dados válidos
    Given estou na página do formulário
    When preencho todos os campos corretamente
    Then o sistema deve exibir a mensagem de diagnóstico

  Scenario: Enviar formulário com CPF inválido
    Given estou na página do formulário
    When preencho o CPF inválido "123"
    Then o sistema deve exibir uma mensagem de erro de CPF inválido

  Scenario: Enviar formulário com campos vazios
    Given estou na página do formulário
    When envio o formulário sem preencher os campos obrigatórios
    Then o sistema deve exibir a mensagem "Por favor, preencha todos os campos"

    