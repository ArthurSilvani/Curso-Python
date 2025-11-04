# REFAÇA O DESAFIO 051, lendo o primeiro termo ea razão de uma PA, mostrando
#os 10 primeiros termos da progressão usando a estrutura WHILE

print('=='*20)
print('10 PRIMEIROS TERMOS DA PA')
print('=='*20)

pa = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = pa
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += r
    cont += 1


    

