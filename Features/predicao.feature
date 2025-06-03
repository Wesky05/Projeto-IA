Feature: Avaliação de risco de esquizofrenia

Scenario: Paciente com risco de esquizofrenia
  Given que eu tenho os dados [25, 1, 1, 1]
  When eu faço a predição com o modelo
  Then o resultado deve ser "Esquizofrenia"

Scenario: Paciente sem risco de esquizofrenia
  Given que eu tenho os dados [25, 0, 0, 0]
  When eu faço a predição com o modelo
  Then o resultado deve ser "Não esquizofrenia"
