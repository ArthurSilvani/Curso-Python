#CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS. A CADA PESSOA CADASTRADA
#, O PROGRAMA DEVERÁ PERGUNTAR SE O USUARIO QUE OU NÃO CONTINUAR. NO FINAL, MOSTRAR:
# A- qauntas pessoas tem mais de 18 anos
# B- Quantos homens foram cadastrados
# C- Quantas mulheres tem menos de 20 anos

maior = home = tot20 = 0
while True:
    print('='*20)
    print('CADASTRO DE PESSOA')
    print('='*20)
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual seu sexo [F/M]? ')).upper() 
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        home += 1
    if sexo == 'F' and idade <= 20:
        tot20 += 1
    print('='*20)
    continuar = str(input('Quer continuar [S/N]? ')).upper()
    if continuar == 'N':
        break   
print(f'Total de pessoas maiores de 18 anos cadastradas é de {maior}')
print(f'A quantidade de homens cadastrados é de {home}')
print(f'E temos {tot20} mulheres com menos de 20 anos')



