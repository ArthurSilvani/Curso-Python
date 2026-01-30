dados = dict()
partidas = list()

dados['nomes'] = str(input('Qual o nome do jogador? '))
prt = int(input(f'Quantas partidas {dados["nomes"]} jogou? '))

for c in range( 0, prt):
    partidas.append(int(input(f'     Quantos gols na partida {c+1}? ')))

dados['gols'] = partidas[:]
dados['total'] = sum(partidas)

print('='*30)

print(dados)

print('='*30)

for k, v in dados.items():
    print(f'O campo {k} tem valor {v}!')

print('='*30)

print(f'O jogador {dados["nomes"]} jogou {prt} partidas!')

for i, v in enumerate(dados['gols']):
    if v == 1:
        print(f'        => Na partida {i+1}, fez {v} gol!')
    else:
        print(f'        => Na partida {i+1}, fez {v} gols!')
print(f'O total de gols foi {dados["total"]}!')


