#faça um programa que leia trÊs números e mostre qual é o maior e qual é o menor

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
#VERFICANDO QUEM É O MENOR

menor = n1 

if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
else: 
    print(f'O menor número é: {menor}') 

#VERIFICANDO O MAIOR VALOR
maior = n1

if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
else:
    print(f'O maior número é: {maior}')
