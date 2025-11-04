#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NUMERO
#INTEIRO ENTRE 0 E 5 E PEÇA PARA O USUARIO TENTAR DESCOBRIR 
#QUAL FOI O NUMERO ESCOLHIDO PELO COMPUTADOR. O PROGRAMA DEVERÁ
#ESCREVER NA TELA SE O USUARIO VENCEU OU PERDEU

from random import randint
from time import sleep #COMPUTADOR DORME POR ALGUNS SEGUNDOS

computador = randint (0, 5) #FAZ O CUMPTADOR PENSAR, SORTEAR

print(' -=- '* 20 )
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print(' -=- '* 20 )

n1 = int(input('Em que número eu pensei? '))

print('PROCESSANDO....')
sleep(3)

if n1 == computador:
    print('Você acertou! PARABENS.')
else:
    print('Bah, você errou, tente mais uma vez na proxima. ')

print(f'Eu havia pensado no número {computador}.')
