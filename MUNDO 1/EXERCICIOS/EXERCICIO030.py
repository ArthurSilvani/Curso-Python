#CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU IMPAR

num = int(input('Digite qaulquer numero: '))

resultado = num % 2 #SE DER 0 É PAR SE SER É IMPAR

if resultado == 0:
    print(f'O número {num} é par. ')
else:
    print(f'O número {num} é impar. ')
