#  Integração Python (Pandas) + SQL Pipeline

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-ETL-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)

##  Sobre o Projeto
Este repositório documenta a construção de um pipeline de Engenharia de Dados focado na integração entre **Dataframes (Pandas)** e **Bancos de Dados Relacionais (SQLite)**.

O objetivo foi simular um processo de **ETL (Extract, Transform, Load)** onde dados são extraídos de arquivos brutos (`.csv`), transformados em memória e carregados em tabelas SQL estruturadas, permitindo consultas analíticas diretas via Python.

*Projeto desenvolvido durante a formação de Dados da Asimov Academy.*

---

##  Arquitetura e Fluxo

O script executa as seguintes etapas automatizadas:

1.  **Extract:** Leitura de dados brutos (`bd_data.csv`) utilizando Pandas.
2.  **Transform:**
    * Tratamento de índices.
    * Slicing de dados (Filtragem de linhas específicas).
3.  **Load & SQL Engineering:**
    * Criação automática de tabelas (`CREATE TABLE`).
    * Inserção de dados em lote (`df.to_sql`).
    * Manipulação via DML (`INSERT`, `UPDATE`, `DELETE`) usando cursores.

---

##  Tecnologias e Conceitos Aplicados

* **Python 3.12**
* **Pandas:** Manipulação de Dataframes e exportação (`to_sql`).
* **SQLite3:** Gerenciamento de banco de dados serverless.
* **SQL Transactions:** Controle de atomicidade com `conn.commit()`.
* **Database Cursors:** Execução de queries SQL cruas dentro do ambiente Python.

---

##  Como Executar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/NOME-DO-REPO.git](https://github.com/SEU-USUARIO/NOME-DO-REPO.git)