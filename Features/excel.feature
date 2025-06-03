Feature: Filtragem e busca dos dados no dashboard de pacientes

  Background:
    Given os dados de pacientes carregados no sistema
    
Scenario: Exportar relatório Excel com dados filtrados
  Given os dados de pacientes carregados no sistema
  When eu gero o relatório Excel dos dados filtrados
  Then o arquivo Excel deve conter as colunas "Nome", "CPF", "Gênero", "Histórico de Suicídio", "Histórico Familiar", "Substâncias de Uso", "Predição"
  And o arquivo Excel deve conter exatamente 5 linhas de dados

