import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import polars as pl
import pandas as pd
from utils.style_planilhas  import style_planilhas
from utils.data_padrao import clean_dataframe


# pega raiz do projeto automaticamente

BASE_DIR = Path(__file__).resolve().parents[2]

arquivo = BASE_DIR / "data/planilha_original/transparencia_excel.xls"

#  ler(arquivo .xls do portal vem em html)
df_pd = pd.read_html(arquivo)[0]

# converter para polars
df = pl.from_pandas(df_pd)

# filtro
df_filtrado = df.filter(
    pl.col("Entidade") == "SECRETARIA DE ESTADO DE DESENVOLVIMENTO ECONOMICO"
)

#  criar pasta processed autamaticamente
output_dir = BASE_DIR/ "data"/ "planilha_tratada"
output_dir.mkdir(parents=True, exist_ok=True)

arquivo_saida = output_dir / "secretaria_desenvolvimento_economico.xlsx"

df_filtrado.write_excel(arquivo_saida)

# limpar dados
df_filtrado = clean_dataframe(df_filtrado)

# formatar planilha
style_planilhas(arquivo_saida)

print("Arquivo salvo em:", arquivo_saida)

