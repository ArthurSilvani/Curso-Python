print('=='*20)
print('10 PRIMEIROS TERMOS DA PA')
print('=='*20)

pa = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = pa
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais 
    while cont <= total:
        print(f'{termo} -> ', end='') 
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

