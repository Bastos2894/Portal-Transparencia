#Criação das tabelas no banco de dados utilizando SQLAlchemy 
from sqlalchemy import text
from utils.db import _LOADget_engine

def main():
    ENGINE = _LOADget_engine()

    with ENGINE.begin() as conn:

        # =========================
        # tabela transparencia
        # =========================
        conn.execute(text(f"""
            CREATE TABLE IF NOT EXISTS transparencia (
                id SERIAL PRIMARY KEY,
                cnpj TEXT,
                razao_social TEXT,
                data DATE,
                ano INT,
                mes INT,
                dia INT,
                trimestre INT,
                numero_processo TEXT,
                contrato TEXT,
                num_contrato_orgao TEXT,    
                valor_global NUMERIC,
                objeto TEXT,
                data_inicio DATE,
                data_fim DATE,
                situacao TEXT,
                modalidade TEXT,
                subtipo TEXT,
                tipo_aquisicao TEXT,
                UNIQUE (cnpj, razao_social, data, situacao, modalidade, subtipo, tipo_aquisicao)
            );
            """))

    

        conn.commit() 

    print("✅ Tabela criada com sucesso!")

if __name__ == "__main__":
    main()