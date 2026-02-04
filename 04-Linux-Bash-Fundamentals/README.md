# 🐧 Linux & Bash Fundamentals

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Bash](https://img.shields.io/badge/Shell_Script-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)

##  Sobre o Módulo
Estudo prático sobre o sistema operacional que sustenta a infraestrutura de Big Data e Cloud Computing. O objetivo foi dominar a navegação via terminal (CLI) e manipulação de arquivos sem interface gráfica.

##  Comandos Essenciais Dominados

###  Navegação (Navigation)
| Comando | Função |
| :--- | :--- |
| `pwd` | Mostra o caminho absoluto atual (Print Working Directory). |
| `ls -la` | Lista todos os arquivos, incluindo ocultos e permissões. |
| `cd ..` | Volta para o diretório anterior (Caminho relativo). |
| `cd ~` | Volta para a pasta pessoal (Home) do usuário. |

### 📂 Manipulação de Arquivos (File Management)
| Comando | Função |
| :--- | :--- |
| `mkdir -p pasta/subpasta` | Cria árvore de diretórios completa de uma vez. |
| `touch arquivo.txt` | Cria um arquivo vazio instantaneamente. |
| `cp -r origem destino` | Copia pastas inteiras recursivamente. |
| `mv arq1 arq2` | Move ou renomeia arquivos. |
| `rm -r pasta` | **Cuidado:** Remove diretórios e arquivos permanentemente (sem lixeira). |

### 🔒 Permissões (Permissions)
Entendimento da estrutura `drwx`:
* **d**: Diretório
* **r**: Leitura (Read)
* **w**: Escrita (Write)
* **x**: Execução (Execute)

---
**Ambiente de Estudo:** VirtualBox (Ubuntu Server)