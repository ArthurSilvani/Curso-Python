#FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE NA TELA O 
#VALOR DO SENO, COSSENO E TANGENTE DESSE ANGULO - lembrar de usar
# math.radians em angulos


import math

n = float(input('Digite o angulo que você deseja: '))

print(f'O angulo de {n} tem o SENO de {math.sin(math.radians (n)):.2f}')
print(f'O angulo de {n} tem o COSSENO de {math.cos(math.radians(n)):.2f}')
print(f'O angulo de {n} tem a TANGENTE de {math.tan(math.radians(n)):.2f}')

