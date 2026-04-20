import os 
import yaml
from dotenv import load_dotenv
# função para carregar o arquivo de configuração YAML, substituindo as variáveis de ambiente
# Carrega as variáveis do .env
load_dotenv()

def load_config(path="config/config.yaml"):

    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    with open(path, "r") as f:
        config = yaml.safe_load(f)

    # 👇 CORREÇÃO IMPORTANTE
    if config is None:
        raise ValueError(f"O arquivo {path} está vazio ou inválido")

    # Substitui variáveis de ambiente ${VAR}
    def replace_env(value):
        if isinstance(value, str) and value.startswith("${"):
            env_var = value.replace("${", "").replace("}", "")
            return os.getenv(env_var)
        return value
    
    for section in config:
        for key in config[section]:
            config[section][key] = replace_env(config[section][key])

    return config