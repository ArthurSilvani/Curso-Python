#faça um programa que tenha uma função chamada maior(), que receba vários paramentros com valores inteiros
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior
from time import sleep

def maior(*num):
    print('-=-'*15)
    print('Analisando os valores passados...')
    sleep(1)
    print(f'{num} Foram informados {len(num)} valores...')
    print(f'O maior valor informado foi {max(num)}!')
    print('-=-'*15)

maior(1, 2, 3, 4, 5)
maior(10, 8, 77, 23, 0)
