#O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE 
#APRESENTAÇÃO DE TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA 
#O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA
import random

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome'))
n4 = str(input('Quarto nome: '))

lista = [n1, n2, n3, n4]
escolher = random.shuffle(lista)

print(f'A ordem de apresentação dos alunos é: {lista}')
