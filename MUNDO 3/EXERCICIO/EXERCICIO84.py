#faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista
# A- Quantas pessoas foram cadastradas
# B- Uma listagem com as pessoas mais pesadas.
# C- Uma listagem com as pessoas mais leves
pessoas = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
   
    continuar = str(input('Quer continuar [S/N]? ')).upper()
    if continuar == 'N' or continuar != 'S':
        break
print(f'O número de pessoas cadastradas foi de {len(pessoas)}')
pesadas = leves = 0
pessoas_pesadas = []
pessoas_leves = []
for p in pessoas:
    if p[1] > pesadas:
        pesadas = p[1]
        pessoas_pesadas.clear()
        pessoas_pesadas.append(p[0])
    elif p[1] == pesadas:
        pessoas_pesadas.append(p[0])

    elif p[1] < leves:
        leves = p[1]
        pessoas_leves.clear()
        pessoas_leves.append(p[0])
    elif p[1] == leves:
        pessoas_leves.append(p[0])

print(f'O maior peso {pesadas} e as pessoas são {pessoas_pesadas}')
print(f'O maior peso {leves} e as pessoas são {pessoas_leves}')