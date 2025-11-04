# ESCREVA UM PROGRAMA PARA APROVAR O EMPRESTIMO BANCARIO PARA A COMPRA
# DE UMA CASA. PERGUNTE O VALOR DA CASA, O SALARIO DO COMPRADOR E 
# EM QUANTOS ANOS ELE VAI PAGAR
# A PRESTAÇÃO MENSAL, NÃO PODE EXCEBER 30% DO SALÁRIO OU ENTÃO EMPRESTIMO NEGADO

casa = int(input('Qual o valor da casa? '))
salario = int(input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos você deseja pagar? '))

parcela = casa / ( anos * 12 ) #parcela o valor da casa vezes os anos 
minimo = salario * ( 30 / 100) #os 30% do salario

if parcela > minimo:
    print(f'O parcelamento não foi \033[1;31m APROVADO! \033[m')
elif parcela < minimo:
    print(f'O parcelamento foi \033[1;32m APROVADO!!!! \033[m')

print(f'Para pagar a casa de R${casa} o custo mensal será de: R${parcela:.2f}')