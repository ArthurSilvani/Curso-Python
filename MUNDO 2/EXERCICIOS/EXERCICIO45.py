#CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print('''Suas opções:'
\033[2;32m[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura \033[m''')

jogada = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('=-='*15)

print(f'O computador jogou {itens[computador]}.')
print(f'O jogador jogou {itens[jogada]}. ')

print('=-='*15)

if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogada == 0:
        print('NINGUÉM GANHOU!!')
    elif jogada == 1: 
        print('O JOGADOR GANHOU!')
    elif jogada == 2:
        print('O COMPUTADOR VENCE!')

elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogada == 0:
        print('O JOGADOR GANHOU!')
    elif jogada == 1:
        print('NINGUÉM GANHOU!')
    elif jogada == 2:
        print('O JOGADOR GANHOU!')

elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogada == 0:
        print('O COMPUTADOR VENCE!')
    elif jogada == 1: 
        print('O JOGADOR VENCE!')
    elif jogada == 2:
        print('NINGUÉM GANHA!')

elif jogada == 3:
    print('ESSA JOGADA NÃO EXISTE, MEU CARO. HAHAHHA!')









