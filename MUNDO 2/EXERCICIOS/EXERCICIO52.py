#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É
# OU NÃO UM numero primo

num = int(input('Digite um número inteiro: '))

tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print(f'{c}', end=' ')

print(f'O número {num} é divisível {tot}. ')

if tot == 2:
    print(f'Esse numero é primo')
else: 
    print('Esse número não é primo.')