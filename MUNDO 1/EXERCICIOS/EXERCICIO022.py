#crie um programa que leia o nome completo de uma pessoa e mostre
# -O NOME COM TODAS AS LETRAS MAIUSCULAS E MINUSCULAS
# - QUANTAS LETRAS AO TODO SEM CONSIDERAR ESPAÇOS
# - QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = str(input('Digite seu nome completo aqui: ')).strip()

print('Analisando seu nome temos que...')

print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minusculo é: {nome.lower()}')
print(f'O seu nome ao todo tem: {len(nome)}')
print(f'O seu primeiro nome é {nome.find(" ")}')
#lembrar que usa aspas duplas e não simples
