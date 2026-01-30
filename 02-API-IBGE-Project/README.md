# 📊 Analisador de Nomes (IBGE API)

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Requests](https://img.shields.io/badge/API-REST-000000?style=for-the-badge&logo=json&logoColor=white)

##  Sobre o Projeto
Aplicação web interativa desenvolvida para consultar a frequência de nomes brasileiros por década, consumindo dados reais da **API de Serviços do IBGE**.

Este projeto marca a transição do processamento de arquivos locais (CSV) para o consumo de dados vivos na web, aplicando fundamentos de **Arquitetura REST** e **Engenharia de Dados**.

---

## Conceitos Técnicos Aplicados

Este projeto foi construído para validar o estudo teórico sobre comunicações Web:

### 1. Protocolo HTTP e Status Codes
A aplicação gerencia a robustez da comunicação Client-Server tratando os códigos de resposta:
* **2XX (Sucesso):** O JSON é processado e transformado em dados analíticos.
* **4XX (Erro do Cliente):** Tratamento para nomes inexistentes ou URLs mal formatadas.
* **5XX (Erro do Servidor):** Proteção contra falhas no serviço do IBGE.
* **Código:** Implementação de `try/except` com o método `raise_for_status()` da biblioteca `requests`.

### 2. Arquitetura REST & Stateless
* **Statelessness:** Cada consulta de nome é uma transação independente. O script constrói **URIs dinâmicas** (Endpoints) para buscar recursos específicos (ex: `.../nomes/Samuel`), sem depender de sessões anteriores.
* **Params:** Uso de parâmetros na URL para filtrar requisições.

### 3. Parsing e Transformação de Dados
* **JSON Schema:** Navegação em estruturas de dados aninhadas (Listas de Dicionários) retornadas pelo governo.
* **Pandas:** Conversão de dados brutos da web (`JSON`) para estruturas tabulares (`DataFrame`) prontas para análise.

---

##  Stack Tecnológica

* **Python 3.12:** Linguagem base.
* **Requests:** Para requisições HTTP (GET).
* **Streamlit:** Framework para criação do Dashboard interativo e visualização de dados.
* **Pandas:** Manipulação e estruturação dos dados.

---

##  Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o Python instalado.

1. **Clone o repositório e entre na pasta:**
   ```bash
   cd Data-engineering-studies/02-API-IBGE-Project