#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO
#CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIANGULO
#RETANGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA

#SEM IMPORTAÇÃO
'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

h = (co ** 2 + ca ** 2) ** (1/2)

print(f' a {h:.2f}')'''

import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
 
h = math.hypot(co, ca) 

print(f'A Hipotenusa é: {h:.2f}')
