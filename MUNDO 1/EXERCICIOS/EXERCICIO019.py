#UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR
#O QUADR. Faça um programa que ajude ele, lendo o nome deles e 
#escrevendo o nome escolhido

import random

x = str(input('Primeiro aluno: '))
y = str(input('Segundo aluno: '))
z = str(input('Terceiro aluno: '))
c = str(input('Quarto aluno: '))

lista = (x, y, z, c)
escolhido = random.choice(lista)

print(f'O aluno escolhido foi: {escolhido}')

