import moedas

p = float(input('Digite o preço: '))

print(f'A metade de {moedas.moeda(p)} é {(moedas.metade(p, True))}!')
print(f'O dobro de {moedas.moeda(p)} é {(moedas.dobro(p, True))}!')
print(f'Aumentando 10%, temos o valor de {(moedas.aumentar(p, 10, True))}!')
print(f'Diminuindo 5%, temos o valor de {(moedas.diminuir(p, 5, True))}')