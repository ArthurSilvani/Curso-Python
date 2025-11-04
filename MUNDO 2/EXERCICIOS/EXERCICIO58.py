#MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI 'PENSAR' EM UM NÚMERO ENTRE 0 E 10
# SO QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL O NUMERO DE PALPITES
# QUE FORAM NECESSARIOS PARA VENCER

from random import randint
from time import sleep #COMPUTADOR DORME POR ALGUNS SEGUNDOS

computador = randint (0, 10) #FAZ O CUMPTADOR PENSAR, SORTEAR
print(' -=- '* 20 )
print('Vou pensar em um número entre 0 e 10. Tente adivinhar... ')
print(' -=- '* 20 )

n1 = 0
palpites = 0

while n1 != computador:
    n1 = int(input('Em que número eu pensei? '))
    palpites += 1
    if n1 > computador:
        print(f'Menos... Tente mais uma vez...')
    elif n1 < computador:
        print(f'Mais... Tente mais uma vez...')

print(f'O número {n1} é o mesmo que eu pensava!. Você chutou {palpites} vezes!. ')
       

