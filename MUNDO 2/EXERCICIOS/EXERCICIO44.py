# ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO
# CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO
# à VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
# À VISTA NO CARTÃO: 5% DE DESCONTO
# EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
# 3X OU MAIS NO CARTÃO: 20% DE JUROS

print('='*30)
print('\033[3;32;43m $ LOJA DO SILVANI $ \033[m')
print('='*30)

preço = float(input('Preço das compras: R$ '))

print('FORMA DE PAGAMENTO')
print('[1] Pagamento à vista/cheque.  |')
print('[2] Pagamento no cartão.       |')
print('[3] Pagamento em 2x.           |')
print('[4] Pagamento em 3x ou mais.   |')
print('='*30)

opção = int(input('Qual a opção? '))

if opção == 1:
    print('| 1 DINHEIRO | ou | 2 CHEQUE |')
    dc = str(input('Qual forma de pagamento você prefere? '))
    dinheiro = preço - ( preço * (10 / 100) ) 
    print(f'Sua compra de R$ {preço} à vista ficará R$ {dinheiro}.')

elif opção == 2:
    cartão = preço - ( preço * (5 / 100))
    print(f'Sua compra de R$ {preço} no cartão será R$ {cartão}.')

elif opção == 4:
    vezes = preço + ( preço * (20 / 100))

    x = int(input('Quantas parcelas? '))
    parcela = vezes / x 
    print(f'Seu parcelamento de {x} fica no valor de R$ {parcela} ')

elif opção == 3:
    print(f'Seu valor continuará {preço} e em 2x será {preço / 2}.')

else: 
    print('\033[2;33m NÃO EXISTE ESSA OPÇÃO \033[m')

    





