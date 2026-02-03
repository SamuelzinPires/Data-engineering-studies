import base64
import requests
from pprint import pprint

usuario = "meu-usuario"
senha = "senha-secreta"

# Cria a string "usuario:senha" e converte para bytes
auth_string = f'{usuario}:{senha}'.encode()

# Transforma em Base64
auth_string = base64.b64encode(auth_string)

# Volta para texto normal (string)
auth_string = auth_string.decode()

#Estrutura para o httpbin 
url = "https://httpbin.org/basic-auth/meu-usuario/senha-secreta"

#Fazendo a atorização basica, não tão segurro...  
headers = {
    'Authorization': f'Basic {auth_string}'
}
resposta = requests.get(url=url, headers=headers)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f'Erro no request: {e}')
    resultado = None
else:
    resultado = resposta.json()

pprint(resultado) 