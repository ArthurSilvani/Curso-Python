#A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA
# QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA, DE
# ate 9 anos MIRIM - ATÉ 14 ANO: INFANTIL 
# ATÉ 19 ANOS - JUNIOR
# ATÉ 25 ANOS SÊNIOR
# acima MASTER

n1 = int(input('Qual o ano que você nasceu? '))

idade = 2025 - n1
print(f'A idade do Atleta é: {idade}.')

if idade <= 9: 
    print('Sua classificação é MIRIM.')
elif idade >= 9 and idade <= 14:
    print('Sua classificação é INFANTIL.')
elif idade >= 15 and idade <= 19: 
    print('Sua classificação é JÚNIOR.')
elif idade >= 20 and idade <= 25:
    print('Sua classificação é SÊNIOR.')
else:
    print('Sua classificação é MASTER.')