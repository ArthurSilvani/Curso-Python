#DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA
# NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO

print('=='*20)
print('10 PRIMEIROS TERMOS DA PA')
print('=='*20)

pa = int(input('Primeiro termo: '))

r = int(input('Razão: '))

for c in range(pa, r*10 , r):
    print(f'{c}', end=' -> ') 
print('ACABOU')