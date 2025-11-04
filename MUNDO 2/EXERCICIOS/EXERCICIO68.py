#FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O COMPUTADO. 
# O J0GO SO SERÁ INTERROMPIFO QUANDO O JOGADOR PERDER, mostrando o total de vitorias consecutivas
# que ele conquistou no final do jogo

print('='*20)
print('JOGAR PAR OU IMPAR')
print('='*20)

from random import randint

ganhos = 0


while True:
    jogador = int(input('Digite um valor: '))
    jogada = str(input('Par ou Ímpar [P/I]? ')).upper()
    
    cpu = randint(1, 10)
    
    total = jogador + cpu
    par = total % 2 
    impar = total % 2
    
    if par == 0:
        print('='*20)
        print(f'Você jogou {jogador} e o computador {cpu}. Total é de {total} e o número é PAR')
        print('='*20)
    elif impar == 1:
         print('='*20)
         print(f'Você jogou {jogador} e o computador {cpu}. Total é de {total} e o número é ÍMPAR')
         print('='*20)
    
    if jogada == 'P':
        if par == 0:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            ganhos += 1
        else:
            print('Você PERDEU')
            break
    elif jogada == 'I':
        if impar == 1:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            ganhos += 1
        else:
            print('Você PERDEU!')
            break
    else:
        break

print('-=-'*20)
print('GAME OVER :( ')
print(f'Você teve strek de {ganhos} vitórias. PARABÉNS')
        




