#import os  (variaveis de anbiente)

import requests
from pprint import pprint
#Biblioteca para variaveis de anbiente, procurando o aquivo com o nome .env
#import dotenv

#Caso fosse utilizar o dotenv
# dotenv.load_dotenv()
# token = os.environ['CHAVE_API_OPENWEATHER']

#OpenWeather : api utilizada 
token = xxx

#Criado como um parametro na url 
url = "http://apiopenweathermap.org/data/2.5/weathger"

# Q = Query
params = {
    'apiid': token,
    'q': 'Goiânia',
    'units': 'metric',
}
resposta = requests.get(url=url, params=params)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f'Erro no request: {e}')
    resultado = None
else:
    resultado = resposta.json()

pprint(resultado) 