import moedas

p = float(input('Digite o preço: '))

print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p)}!')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p)}!')
print(f'Aumentando 10%, temos o valor de {moedas.aumentar(p, 10):.2f}!')
print(f'Diminuindo 5%, temos o valor de {moedas.diminuir(p, 5):.2f}')