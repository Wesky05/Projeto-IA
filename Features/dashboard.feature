Feature: Acesso ao Dashboard

  Scenario: Acesso ao dashboard com usuário logado
    Given o usuário está logado
    When acessa a página de dashboard
    Then o sistema deve exibir o nome do usuário na interface

  Scenario: Acesso ao dashboard sem login
    Given não estou logado
    When tento acessar o dashboard
    Then devo ser redirecionado para a página de login
