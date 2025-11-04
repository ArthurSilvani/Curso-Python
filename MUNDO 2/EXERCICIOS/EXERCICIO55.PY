#faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi maior e o menor peso lidos
maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Qual o peso da primeira pessoa? '))

    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}KG.')
print(f'O menor peso lido foi {menor}KG. ')
            