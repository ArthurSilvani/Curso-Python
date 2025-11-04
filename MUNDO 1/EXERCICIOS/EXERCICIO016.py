#Crie um progrma que leia um número Real qualquer pelo teclado
#e mostre na tela a sua porção inteira

from math import trunc 
num = float(input('Digite um número qualquer: '))

print(f' O número {num} tem parte inteira {trunc(num)}')


