#CRIE UM PROGRAMA QUE LEIA O NOME E DUAS NOTAS DE VÁRIOS ALUNOS E 
# GUARDE TUDO EM UMA LISTA COMPOSTA. NO FINAL, MOSTRE UM BOLETIM CONTENDO
#A MÉDIA DE CADA UM E PERMITA QUE O USÚARIO POSSA MOSTRAR AS NOTAS DE CADA ALUNO INDIVIDUALMENTE

ficha = list()

while True:

    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1:' ))
    nota2 = float(input('Nota 2: '))
    media = float(nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    continuar = str(input('Você deseja continuar [S/N]? '))
    if continuar == 'Nn':
        break

print('-' *20)
print(f'{"No":<10}{"Nome":<10}{"Média":<10}')
print('-' *20)

for i, a in enumerate(ficha):
    print(f'{i:<10}{a[0]:<10}{a[2]:<10}')

while True:
    print('-'*20)
    opc = int(input('Mostrar notas de qual dos alunos? (999 para): '))
    if opc == '999':
        print('Finalizan...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

print('<<<<< Volte Sempre <<<<<<<<<<')