#REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUARIO
# ESCOLHE, SO QUE UTILIZANDO UM LAÇO FOR
x = int(input('Digite o número para ver sua tabuada: '))

for c in range(1, 11):
    print(f'{x} x {c} = {x*c}')


    