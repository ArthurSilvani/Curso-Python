#FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU
#NOVO PREÇO, COM 5% DE DESCONTO

v = float(input('Qual o valor da compra? R$'))

desc = (v * 5) / 100

final = v - desc

print(f'Seu desconto é de {desc:.2f}, com o valor final de {final:.2f}')
