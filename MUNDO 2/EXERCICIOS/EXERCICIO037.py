# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA
# PARA O USUARIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO:
# 1 - PARA BINARIO
# 2 - PARA OCTAL
# 3 - PARA HEXADECIMAL

num = int(input('Digite algum número: '))

print('''Escolha uma base de Conversão:' 
[1] BINÁRIO 
[2] OCTAL
[3] HEXADECIMAL''')

opçao = int(input('Sua opção: '))

if opçao == 1:
    print(f'O {num} binário é {bin(num)[2:]}')
elif opçao == 2:
    print(f'O {num} octal é {oct(num)[2:]}')
elif opçao == 3:
    print(f'O {num} hexadecimal é {hex(num)[2:]}')
else:
    print('Opção INVÁLIDA')