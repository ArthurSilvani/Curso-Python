# faça um programa que ajude um jogador da mega sena criar palpites, o programa vai perguntar 
#quantas jogadas serão geradas e vai sortear 6 numeros entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint

lista = list()
jogos = list()
 
print('-'*10)
print('     JOGOS DA MEGA SENA      ')
print('-'*10)

quant = int(input('Quantos jogos voce quer que eu sortei? '))
tot = 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    lista.append(list[1])
    tot += 1

print(f'SORTEANDO {quant} JOGOS')

for i, l in enumerate(jogos):
    print(f'Jogos {i+1}: {l}')
