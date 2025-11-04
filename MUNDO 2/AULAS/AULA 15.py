# INTERROMPENDO REPETIÇÕES WHILE 

'''cont = 1

while True:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''

n = s = 0 

while True:
    n = int(input('Digite um número: '))
    
    if n == 999:
        break
    
    s += n #SOMANDO OS 'N' , soma = soma + n, soma = 0 + n

print(f' A soma vale {s}.')