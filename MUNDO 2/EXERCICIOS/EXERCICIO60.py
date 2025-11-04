#calculando fatorial 

import math 

fatorial = int(input('Digite um número para calcular fatorial: '))
resultado = math.factorial(fatorial)
c = fatorial 

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1

print(f'O valor da fatorial de {fatorial} é igual a: {resultado}. ')