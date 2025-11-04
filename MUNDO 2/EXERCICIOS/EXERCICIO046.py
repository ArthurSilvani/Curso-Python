#FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O 
# ESTOURO DE FOGOS DE ARTIFICIO, INDO DE 10 ATÉ 0, COM UMA PAUSA DE 1s ENTRE ELES.

from time import sleep

print('='*22)
print('CONTEGEM REGRESSIVA')
print('='*22)

for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('fim')
