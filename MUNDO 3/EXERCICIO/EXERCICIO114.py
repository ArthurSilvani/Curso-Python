#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import requests

try:
    resposta = requests.get("http://www.pudim.com.br", timeout=5)

    if resposta.status_code == 200:
        print('O site está acessível! ')

    else:
        print(f"O site respondeu, mas com código: {resposta.status_code}")
    
except requests.ConnectionError:
    print("Não foi possível conectar ao site. ❌")

except requests.Timeout:
    print("O site demorou para responder. ⏳")

except requests.RequestException as erro:
    print(f"Ocorreu um erro: {erro}")