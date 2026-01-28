#APRIMORE O DESAFIO ANTERIOR, MOSTRANDO NO FINAL:
#A- A SOMA DE TODOS OS VALORES PARES DIGITADOS
#B - A SOMA DOS VALORES DA TERCEIRA COLUNA
#C - O MAIOR VALOR DA SEGUNDA LINHA

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))

print('=-'*10)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()