#FAÇA UM PROGRMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS IMPARES QUE
# SÃO MULTIPLOS DE TRêS E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500
 
soma = 0 #ACUMULADORES
cont = 0
for c in range(1, 501, 2,):
    if c % 3 == 0: #RESTO PARA SABER SE É MULTIPLO
        cont = cont + 1
        soma = soma + c
print(f'A soma dos {cont} valores solicitados é {soma}.')    