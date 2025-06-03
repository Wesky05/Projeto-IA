Feature: Filtros individuais no dashboard de pacientes

  Background:
    Given os dados de pacientes estão carregados no sistema

  # ---------- Filtro de Gênero ----------
  Scenario: Filtrar pacientes por gênero Masculino
    When eu aplico o filtro de gênero "Masculino"
    Then deve exibir apenas pacientes do gênero "Masculino"

  Scenario: Filtrar pacientes por gênero Feminino
    When eu aplico o filtro de gênero "Feminino"
    Then deve exibir apenas pacientes do gênero "Feminino"

  Scenario: Filtrar pacientes por gênero Todos
    When eu aplico o filtro de gênero "Todos"
    Then deve exibir todos os pacientes, independente do gênero


  # ---------- Filtro de Histórico de Suicídio ----------
  Scenario: Filtrar pacientes com histórico de suicídio Sim
    When eu aplico o filtro de histórico de suicídio "Sim"
    Then deve exibir apenas pacientes com histórico de suicídio "Sim"

  Scenario: Filtrar pacientes com histórico de suicídio Não
    When eu aplico o filtro de histórico de suicídio "Não"
    Then deve exibir apenas pacientes com histórico de suicídio "Não"

  Scenario: Filtrar pacientes com histórico de suicídio Todos
    When eu aplico o filtro de histórico de suicídio "Todos"
    Then deve exibir todos os pacientes, independente do histórico de suicídio


  # ---------- Filtro de Histórico Familiar ----------
  Scenario: Filtrar pacientes com histórico familiar Sim
    When eu aplico o filtro de histórico familiar "Sim"
    Then deve exibir apenas pacientes com histórico familiar "Sim"

  Scenario: Filtrar pacientes com histórico familiar Não
    When eu aplico o filtro de histórico familiar "Não"
    Then deve exibir apenas pacientes com histórico familiar "Não"

  Scenario: Filtrar pacientes com histórico familiar Todos
    When eu aplico o filtro de histórico familiar "Todos"
    Then deve exibir todos os pacientes, independente do histórico familiar


  # ---------- Filtro de Substâncias de Uso ----------
  Scenario: Filtrar pacientes que usam substâncias Sim
    When eu aplico o filtro de substâncias de uso "Sim"
    Then deve exibir apenas pacientes que usam substâncias "Sim"

  Scenario: Filtrar pacientes que usam substâncias Não
    When eu aplico o filtro de substâncias de uso "Não"
    Then deve exibir apenas pacientes que usam substâncias "Não"

  Scenario: Filtrar pacientes por substâncias Todos
    When eu aplico o filtro de substâncias de uso "Todos"
    Then deve exibir todos os pacientes, independente do uso de substâncias


  # ---------- Filtro de Predição ----------
  Scenario: Filtrar pacientes com predição Sim
    When eu aplico o filtro de predição "Sim"
    Then deve exibir apenas pacientes com predição "Sim"

  Scenario: Filtrar pacientes com predição Não
    When eu aplico o filtro de predição "Não"
    Then deve exibir apenas pacientes com predição "Não"

  Scenario: Filtrar pacientes por predição Todos
    When eu aplico o filtro de predição "Todos"
    Then deve exibir todos os pacientes, independente da predição


  # ---------- Filtro de CPF ----------
  Scenario: Buscar paciente pelo CPF existente
    When eu busco pelo CPF válido
    Then deve exibir apenas o paciente correspondente ao CPF informado

  Scenario: Buscar paciente por CPF inexistente
    When eu busco por um CPF inexistente
    Then não deve exibir nenhum paciente
