import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import polars as pl
import pandas as pd

from utils.style_planilhas import style_planilhas
from utils.data_padrao import clean_dataframe
from utils.config_loader import load_config

# base
BASE_DIR = Path(__file__).resolve().parents[1]

config = load_config()

arquivo = BASE_DIR / config["paths"]["input"]
output_dir = BASE_DIR / config["paths"]["output"]
entidade = config["filtro"]["entidade"]
nome_saida = config["excel"]["nome_saida"]

output_dir.mkdir(parents=True, exist_ok=True)
arquivo_saida = output_dir / nome_saida

# valida arquivo
if not arquivo.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")

# ler
df_pd = pd.read_html(arquivo)[0]
df = pl.from_pandas(df_pd)

# valida coluna
if "Entidade" not in df.columns:
    raise ValueError("Coluna 'Entidade' não encontrada no arquivo.")

# filtro
df_filtrado = df.filter(pl.col("Entidade") == entidade)

# limpeza
df_filtrado = clean_dataframe(df_filtrado)

# exportar
df_filtrado.write_excel(arquivo_saida)

# estilo
style_planilhas(arquivo_saida)

print("Arquivo salvo em:", arquivo_saida)