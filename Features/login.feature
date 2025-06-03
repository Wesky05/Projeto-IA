Feature: Login Administrativo

  Scenario: Login bem-sucedido com credenciais válidas
    Given o sistema está rodando
    When eu envio usuário "admin" e senha "senha123" para login
    Then devo ser redirecionado para o dashboard

  Scenario: Login falha com credenciais inválidas
    Given o sistema está rodando
    When eu envio usuário "admin" e senha "senhaErrada" para login
    Then devo receber uma mensagem de erro "Usuário ou senha incorretos"
