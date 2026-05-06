# 📊 Projeto Transparência — Pipeline de Dados (ETL)

Este projeto implementa um pipeline de **ETL (Extract, Transform, Load)** para processamento de dados de transparência pública, integrando arquivos CSV e Excel e carregando-os em um banco de dados estruturado.

---

## 🚀 Objetivo

Organizar, tratar e armazenar dados públicos de transparência para possibilitar análises, dashboards e geração de insights.

---

## 🏗️ Estrutura do Projeto

```
projeto_bi/
├── Scripts/                 # Scripts do pipeline ETL
│   ├── start.py            # Orquestrador principal
│   ├── 01_read.py          # Leitura dos dados
│   ├── 01_create_tables.py # Criação das tabelas
│   ├── 02_load_data.py     # Carga dos dados
│   └── 03_constraints.py   # (Opcional) Constraints do banco
│
├── utils/                  # Funções auxiliares
│   ├── config_loader.py    # Leitura de configurações YAML
│   ├── db.py               # Conexão com banco de dados
│   ├── data_padrao.py      # Padronização de dados
│   └── style_planilhas.py  # Formatação de planilhas
│
├── config/                 # Arquivos de configuração
│   └── config.yaml
│
├── data/                   # Dados de entrada
│   ├── arquivo_csv/
│   └── planilha_tratada/
│
├── docker-compose.yaml     # Configuração de containers
├── requirements_full.txt   # Dependências Python
└── test.py                 # Script de testes
```

---

## ⚙️ Como funciona o Pipeline

O pipeline é executado a partir do script principal:

```bash
python Scripts/start.py
```

### Etapas executadas:

1. **Leitura dos dados**

   * Importa dados CSV e Excel

2. **Criação das tabelas**

   * Estrutura o banco de dados

3. **Carga de dados**

   * Insere dados tratados no banco

4. *(Opcional)* Aplicação de constraints

   * Integridade referencial (PK, FK)

---

## 🐳 Execução com Docker

Para subir o ambiente completo:

```bash
docker-compose up -d
```

---

## 🧰 Tecnologias Utilizadas

* Python
* Pandas
* SQLAlchemy
* OpenPyXL
* Docker
* YAML

---

## 📥 Entrada de Dados

O sistema trabalha com:

* Arquivos **CSV**
* Planilhas **Excel**

Localizados na pasta:

```
data/
```

---

## 📤 Saída

Os dados processados são armazenados em um banco de dados configurado via `config.yaml`.

---

## 🔧 Configuração

Edite o arquivo:

```
config/config.yaml
```

Para definir:

* Conexão com banco
* Caminhos de arquivos
* Parâmetros do pipeline

---

## ⚠️ Observações

* O script `03_constraints.py` não é executado automaticamente
* Recomenda-se adicionar logs estruturados para produção
* Nomes dos scripts podem ser padronizados para melhor organização

---

## 📌 Melhorias Futuras

* Implementar logging com `logging`
* Criar testes automatizados
* Adicionar validação de dados
* Documentar modelo do banco
* Padronizar nomenclatura dos scripts

---

## 👨‍💻 Autor

Projeto desenvolvido para processamento e análise de dados públicos de transparência.

---

## 📄 Licença

Este projeto pode ser utilizado para fins educacionais e de análise de dados públicos.

---
