#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO 'N' INTEIRO QUALQUER E MOSTRE
# NA TELA OS N PRIMEIROS ELEMENTOS DE UMA sequencia de fibonacci

print('-'*20)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*20)

qnt = int(input('Quantos termos você quer mostrar? '))

mais = 1
t1 = 0
t2 = 1
t3 = t1 + t2
print('-'*30)

print(f'{t1} -> {t2} -> ', end='')

cont = 3

while cont <= qnt:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    t1 = t2 
    t2 = t3
    cont +=1
print('-> FIM')