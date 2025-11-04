#Escreva um programa que pergunte a quantidade de KM percorridos por um 
#carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule
# o preço a pagar, sabendo que o carro custa R$60 por dia e 0.15 por KM rodado

dias = float(input('Número de dias usando o carro: '))

km = float(input('Quantos KM percorridos? '))

f = (dias * 60) + (km * 0.15)

print(f' O total a ser pago é de: R${f:.2f}')