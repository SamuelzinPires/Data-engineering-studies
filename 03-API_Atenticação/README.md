# 🔐 Estudos de Segurança: Autenticação em APIs

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/CyberSecurity-API_Auth-black?style=for-the-badge&logo=auth0&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-003B57?style=for-the-badge&logo=python&logoColor=white)

## 📌 Sobre o Módulo
Este módulo documenta o estudo prático sobre **Segurança e Autenticação no consumo de APIs REST**. 

Enquanto APIs públicas (como a do IBGE) permitem acesso livre, a maioria das APIs de mercado (como Spotify, AWS, Bancos) exige validação de identidade. O objetivo destes scripts é servir como "Cheatsheet" (guia de consulta) para os principais métodos de autenticação do mercado.

---

##  Conceitos Técnicos e Boas Práticas

### 1. Basic Auth (Autenticação Básica)
* **Conceito:** Envio de credenciais (usuário e senha) diretamente no cabeçalho (`Header`) da requisição HTTP.
* **Mecânica:** As credenciais são concatenadas no formato `usuario:senha` e codificadas em **Base64** antes do envio.
* **Script de Referência:** `Autenticação - Básica.py`

### 2. Bearer Auth (Autenticação por Token)
* **Conceito:** O cliente envia um Token de Acesso (geralmente uma API Key ou JWT) que "autoriza" a requisição sem enviar a senha original.
* **Mecânica:** O token é passado no Header (`Authorization: Bearer <token>`) ou como parâmetro da URL.
* **Script de Referência:** `Autenticação - Bearer.py`

### 3. Segurança de Dados (Data Privacy) 
A regra de ouro aprendida neste módulo: **Nunca versionar credenciais no código-fonte (Hard-coding).**
* Uso da biblioteca `python-dotenv` para carregar variáveis de ambiente.
* Armazenamento de tokens em arquivos `.env` locais.
* Proteção obrigatória do arquivo `.env` através do `.gitignore`.

---

## 📂 Estrutura dos Scripts

* `Autenticação - Básica.py`: Demonstra o processo de Encode/Decode usando a biblioteca padrão `base64` do Python e consumo do simulador `httpbin.org`.
* `Autenticação - Bearer.py`: Template de consumo de API (OpenWeather) utilizando parâmetros de query e preparação para variáveis de ambiente (`os.environ`).

---
**Engenharia de Dados - Trilha de Estudos**