import os, json
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
import pandas as pd

dotenv=find_dotenv()
load_dotenv(dotenv)

cic_settings = json.loads(os.environ.get("CIC_SETTINGS", {}))
erp_settings = json.loads(os.environ.get("ERP_SETTINGS", {}))
venda_settings = json.loads(os.environ.get("VENDA_SETTINGS", {}))

CORE_PATH = os.getcwd()
SQL_PACKAGE_PATH = os.path.join(CORE_PATH, "sql")

class DbManager:
    def __init__(self, db_setting=None):
        """Inicialize uma conexão com um banco de dados."""

        self.db_setting = db_setting
        user = self.db_setting["user"]
        password = self.db_setting["password"]
        host = self.db_setting["host"]
        port = self.db_setting["port"]
        database = self.db_setting["database"]
        options = self.db_setting["options"]

        # Crie a string de conexão
        connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'

        # Crie a engine usando a string de conexão
        self.engine = create_engine(connection_string, client_encoding='utf8')
    
        print(self.engine)
    def execute_query(self, query_name):
        """Execute consultas e receba DataFrames em troca."""
        with open(os.path.join(SQL_PACKAGE_PATH, query_name), "r", encoding="utf-8") as sql_file:
            q = sql_file.read()
            print(q)
            _df = pd.read_sql(q, self.engine)
            return _df