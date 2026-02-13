import moedas

p = float(input('Digite o preço: '))

print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}!')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}!')
print(f'Aumentando 10%, temos o valor de {moedas.moeda(moedas.aumentar(p, 10))}!')
print(f'Diminuindo 5%, temos o valor de {moedas.moeda(moedas.diminuir(p, 5))}')