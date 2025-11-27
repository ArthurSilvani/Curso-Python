#CRIE UM PROGRAMA ONDE O USÚARIO POSSA DIGITAR 7 VALORES E CADASTRE-OS EM UMA LISTA ÚNICA
# que MANTENHA SEPARADOS OS VALORES PARES E IMPARES. NO FINAL MOSTRE OS VALORE PARES E IMPARES EM ORDEM CRESCENTE

lista = [ [],[] ]
for c in range(1, 8):
    lista.append(int(input(f'Digite o {c}° número: ')))
    if c % 2 == 0:
        lista[0].append(c)
    else:
        lista[1].append(c)
lista[1].sort()
lista[0].sort()
print(f'Os valores pares são {lista[0]}!')
print(f'Os valores impares são {lista[1]}!')