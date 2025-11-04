# REFAÇA O DESAFIO 035 DOS TRIANGULOS, ACRESCENTANDO O RECURSO DE
# MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO:
# EQUILÁTERO: TODOS LADOS IGUAIS
# ISOSCELES: DOIS LADOS IGUAIS
# ESCALENO: TODOS OS LADOS DIFERENTES

n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os  segmentos acima PODEM FORMAR triângulo! ', end='')
    if n1 == n2 == n3:
        print('Esse triângulo é um EQUILÁTERO!')
    elif n1 != n2 != n3 != n1:
        print('Esse triângulo é um ESCALENO!')
    else:
        print('Esse triangulo é ISOSCELES!')


