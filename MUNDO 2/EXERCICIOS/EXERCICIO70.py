#CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR SE O
#USÁRIO VAI CONTINUAR. NO FINAL, MOSTRE:
# A- QUAL É O TOTAL GASTO NA COMPRA
# B- QUNTOS PRODUTOS CUSTAM MAIS DE R$1000 
# C- QUAL É O NOME DO PRODUTO MAIS BARATO

total = maior = menor = cont = 0
barato = '' #barato não é nem um prfuto
while True:
    nomeprt = str(input('Nome do produto: '))
    valor = int(input('Preço: R$ '))
    
    total += valor
    cont += 1

    if valor >= 1000:
        maior += 1
    
    if cont == 1 or valor < menor:
        menor = valor 
        barato = nomeprt

    continuar = str(input('Quer continuar [S/N]? ')).upper()
    if continuar == 'N':
        break
print(f'O gasto total foi de R${total}')
print(f'Houve {maior} valores maiores que R$ 1000,00. ')
print(f'O produto mais barato foi {nomeprt} custando {valor}')

