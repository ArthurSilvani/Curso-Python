#AULA DE CONDIÇÕES IF e ELSE

"""nome = str(input('Qual é o seu nome? '))
if nome == 'Arthur':
    print('Que nome lindo que você tem. ')
else:
     print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2 

print(f'A sua média foi {m:.1f}.')

if m >= 6.0:
    print(f'Sua média foi boa! Parabens.')
else:
    print(f'Sua média foi ruim. Estude mais!')