#CRIE UM PROGRAMA QUE LEIA VÁRIOS NUMEROS INTEIROS PELO TECLADO. O PROGRAMA SO VAI PARAR QUANDO O USUARIO DIGITAR
# O VALOR DE 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS 
# E QUAL FOI A SOMA ENTRE ELES, ( DESCONSIDERANDO O 999 que é o flag)

n = cont = s = 0

while True:
    n = int(input('Digite um número ( 999 para parar): '))

    if n == 999:
        break
    
    cont += 1
    s += n

print(f'A soma dos {cont} valores é de {s}.')