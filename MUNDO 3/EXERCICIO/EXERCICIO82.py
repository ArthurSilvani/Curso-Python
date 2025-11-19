#CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS E COLOQUE EM UMA LISTA.
# DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS QUE VÃO CONTER APENAS OS VALORES PARES E OS VALORES IMPARES DIGITADOS RESPECTIVAMENTE
# AO FINA, MOSTRE O CONTÉUDO DAS TRÊS LISTAS GERADAS

listona = list()
pares = list()
impar = list()

while True:
    num = (int(input('Digite um valor: ')))
    listona.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impar.append(num)

    continuar = input('Você deseja continuar [S/N]? ').upper()
    if continuar == 'N':
        break
pares.sort()
impar.sort()
listona.sort()
print(f'A lista completa é {listona}!')
print(f'A lista par é {pares}')
print(f'A lista impar é {impar}')
