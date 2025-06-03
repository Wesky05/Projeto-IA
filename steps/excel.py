from behave import given, when, then
import pandas as pd
import io

@given("os dados de pacientes carregados no sistema")
def step_impl_carregar_dados(context):
    context.dados = pd.DataFrame({
        "Nome": ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"],
        "CPF": ["111.111.111-11", "222.222.222-22", "333.333.333-33", "444.444.444-44", "555.555.555-55"],
        "Gênero": ["Feminino", "Masculino", "Masculino", "Feminino", "Masculino"],
        "Histórico de Suicídio": ["Sim", "Não", "Não", "Sim", "Não"],
        "Histórico Familiar": ["Não", "Sim", "Não", "Sim", "Não"],
        "Substâncias de Uso": ["Não", "Sim", "Não", "Sim", "Não"],
        "Predição": [1, 0, 0, 1, 0]
    })
    # Inicialmente sem filtro
    context.filtrados = context.dados

@when("eu gero o relatório Excel dos dados filtrados")
def step_when_gerar_excel(context):
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        context.filtrados.to_excel(writer, sheet_name='Pacientes', index=False)
        writer.save()
    buffer.seek(0)
    context.excel_buffer = buffer

@then('o arquivo Excel deve conter as colunas {colunas}')
def step_then_validar_colunas_excel(context, colunas):
    col_list = [c.strip().strip('"') for c in colunas.split(",")]
    df_excel = pd.read_excel(context.excel_buffer)
    assert list(df_excel.columns) == col_list, f"Colunas no Excel: {list(df_excel.columns)}, esperado: {col_list}"

@then('o arquivo Excel deve conter exatamente {qtd:d} linhas de dados')
def step_then_validar_qtd_linhas_excel(context, qtd):
    df_excel = pd.read_excel(context.excel_buffer)
    assert len(df_excel) == qtd, f"Excel tem {len(df_excel)} linhas, esperado: {qtd}"
