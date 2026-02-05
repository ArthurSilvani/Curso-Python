dados = dict()
partidas = list()
time = list()
nome = list()

while True: 
    dados.clear()
    dados['nome'] = str(input('Qual o noem do jogador? '))
    prt = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    for c in range(0 , prt):
        partidas.append(int(input(f'     Quantos gols na partida {c+1}? ')))
    
    dados['gols'] = partidas[:]
    dados['total'] = sum(partidas)
    time.append(dados.copy())
    nome.append(dados['nome'])


    while True:
        continuar = str(input('Você deseja continuar [S/N]: '))
        if continuar in 'SN':
            break
        print('Erro! Digite apenas S ou N !')
    if continuar == 'N':
        break

print('COD  NOME        GOLS        TOTAL')

for k, i in enumerate(time):
    print(f'{k:<2}', end='')
    for d in i.values():
        print(f'{str(d):<12}', end='')


while True:
    busca = int(input('Mostrar dados de qual jogador (999 para): '))
    if busca == 999:
        break