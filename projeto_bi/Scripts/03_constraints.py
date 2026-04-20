# # Script para adicionar uma constraint de unicidade na tabela "transparencia" do banco de dados. A constraint garante que a combinação dos campos "numero_processo", "contrato" e "num_contrato_orgao" seja única, evitando a inserção de registros duplicados.
# from utils.db import _LOADget_engine
# from sqlalchemy import text

# engine = _LOADget_engine()

# with engine.connect() as conn:
    
#     conn.execute(text("""
#         ALTER TABLE transparencia
#                       ADD CONSTRAINT unique_contrato UNIQUE (
#                       numero_processo,
#                       contrato,
#                       num_contrato_orgao );
#     """))

#     conn.commit()

# print("Constraint added successfully.")