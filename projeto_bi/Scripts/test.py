# Script para testar a conexão com o banco de dados utilizando a função get_engine do módulo utils.db. O script tenta estabelecer uma conexão e imprime uma mensagem de sucesso se a conexão for bem-sucedida.
from utils.db import get_engine

engine = get_engine()

with engine.connect() as conn:
    print("✅ Conectado com sucesso!")
    print("🔍 Verificando a versão do banco de dados...")
    version = conn.execute("SELECT version()").fetchone()
    print(f"📊 Versão do banco de dados: {version[0]}")