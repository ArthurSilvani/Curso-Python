#faça um programa que leia um ano qualquer e mostre se ele é bissexto

from datetime import date

ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))

bissexto = (ano % 2) and (ano % 100) or (ano % 400), 
if ano == 0:
    ano = date.today().year #IMPORTEI PARA ANALISAR A DATA E HORA DO MEU PC
if bissexto == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO é BISSEXTO.')

