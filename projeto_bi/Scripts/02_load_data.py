# Script para ler o arquivo Excel, limpar os dados, exportar para CSV e inserir no banco de dados. O script também cria o schema no banco se ele não existir.
import pandas as pd
from sqlalchemy import text
from utils.db import _LOADget_engine

def main():
    ENGINE = _LOADget_engine()
    SCHEMA = "portal_transparencia_02"

    # =========================
    # 1. LER DADOS
    # =========================
    df = pd.read_excel("data/planilha_tratada/secretaria_desenvolvimento_economico.xlsx")

    # =========================
    # 2. LIMPEZA
    # =========================

    # CNPJ
    df['cnpj'] = (
        df['cnpj']
        .astype(str)
        .str.replace(r'\D', '', regex=True)
        .str.zfill(14)
    )

    # VALOR
    df['valor_global'] = (
        df['valor_global']
        .astype(str)
        .str.replace('.', '', regex=False)
        .str.replace(',', '.', regex=False)
    )
    df['valor_global'] = pd.to_numeric(df['valor_global'], errors='coerce')

    # DATAS
    df['data_de_celebracao'] = pd.to_datetime(
        df['data_de_celebracao'], dayfirst=True, errors='coerce'
    )

    df[['data_inicio', 'data_fim']] = df['data_de_vigencia'].str.split(' a ', expand=True)

    df['data_inicio'] = pd.to_datetime(df['data_inicio'], dayfirst=True, errors='coerce')
    df['data_fim'] = pd.to_datetime(df['data_fim'], dayfirst=True, errors='coerce')

    # =========================
    # 3. AJUSTES FINAIS
    # =========================

    df = df.rename(columns={
        "numero_do_processo": "numero_processo"
    })

    df = df.drop_duplicates()

    # =========================
    # 4. EXPORTAR CSV
    # =========================
    df.to_csv(
        "data/arquivo_csv/transparencia_final.csv",
        index=False,
        sep=';',
        encoding='utf-8-sig'
    )
    # ========================
    # 5. CRIA O SCHEMA SE NÃO EXISTIR
    # =========================
    with ENGINE.connect() as conn:
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA};"))
        conn.commit()


    print(df.shape)
    print(df.head())
    # =========================
    # 6. INSERT NO BANCO (UMA TABELA SÓ)
    # =========================
    df.to_sql(
        "transparencia",
        ENGINE,
        schema=SCHEMA,
        if_exists="replace",  # ou "append" se quiser acumular
        index=False,
        method="multi",
        chunksize=1000
    )

    print("✅ Tabela única criada com sucesso")

if __name__ == "__main__":
    main()