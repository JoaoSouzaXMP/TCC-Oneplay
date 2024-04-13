import pyodbc

SECRET_KEY = 'Oneplaypy'

try:
    SERVER = r'.\SQLEXPRESS'
    DRIVER = 'ODBC Driver 17 for SQL Server'
    CONNECTIONSTRING = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE=dbOneplay;Trusted_Connection=yes;'
    CONN = pyodbc.connect(CONNECTIONSTRING, autocommit = True)
    CURSOR = CONN.cursor()
except pyodbc.Error as ex:
    sqlstate = ex.args[0]
    if sqlstate == '42000':
        print("Erro de sintaxe SQL.")
    else:
        print(f"Ocorreu um erro: {ex}")
    exit()