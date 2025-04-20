import pyodbc

try:
    conn_str = (
        "Driver={SQL Server};"
        "Server=KEVIN\\MSSQLSERVER2;"
        "Database=EscolaDB;"
        "Trusted_Connection=yes;"
    )
    conn = pyodbc.connect(conn_str)
    print("✅ Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print("❌ Erro na conexão:", e)
