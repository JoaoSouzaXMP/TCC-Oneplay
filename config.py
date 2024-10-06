import urllib

SERVER = r'.\SQLEXPRESS'
DRIVER = 'ODBC Driver 17 for SQL Server'
CONNECTIONSTRING = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE=dbOneplay;Trusted_Connection=yes;'

PARAMS = urllib.parse.quote_plus(CONNECTIONSTRING)

class Config:
    SECRET_KEY = 'Oneplaypy'
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={PARAMS}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Adicione outras configurações aqui

class DevelopmentConfig(Config):
    DEBUG = True
    # Outras configurações específicas para desenvolvimento

class ProductionConfig(Config):
    DEBUG = False
    # Outras configurações específicas para produção