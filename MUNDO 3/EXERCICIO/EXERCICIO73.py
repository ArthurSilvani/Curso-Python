#CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO BRASILEIRÃO DE FUTEBOL, NA ORDEM DE COLOCAÇÃO. DEPOIS MOSTRE
# A- APENAS OS 5 PRIMEIROS COLOCADOS
# B- OS ÚLTIMOS 4 COLOCADOS
# C- UMA LISTA COM OS TIMES EM ORDEM ALFABÉTICA
# D- EM QUE POSIÇÃO NA TABELA ESTÁ O TIME do GRÊMIO

lista = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo', 'Fluminese',
         'São Paulo', 'Vasco da Gama', 'Corinthians', 'Grêmio', 'Ceara', 'Atletico-MG', 
         'Bragantino', 'Internacional', 'Santos', 'Vitória', 'Fortaleza', 'Juventude', 'SportRecife')

print(f'Lista do Campeonato brasileiro: {lista}')

print('='*150)

print(f' Os cinco primeiros colocados são: {lista[0:6]}') # PARTE A 

print('='*150)

print(f'Os últimos quatros colocados são: {lista[16:21]}') # PARTE B

print('='*150)

print(f'Os times em ordem alfabética é: {sorted(lista)}')

print('='*150)

print(f'O GRÊMIO esta na posição {lista.index("Grêmio") +1 }ª ')




