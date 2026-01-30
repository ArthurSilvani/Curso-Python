#CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VÁRIAS PESSOAS, GUARDANDO
# OS DADOS DE CADA PESSOA EM UM DICIONÁRIO E TODOS OS DICIONÁRIOS EM UMA LISTA.
#NO FINAL, MOSTRE: A- Quantas pessoas foram cadastradas
#B- A média de idade
#C-Uma lista com mulheres
#D- Uma lista com idade acima da média 

dados = dict()
banco = list()
id = list()
mulheres = list()

while True:
    dados.clear()
    dados['nomes'] = str(input('Nome: '))

    while True:
        dados['sexo'] = str(input('Sexo [F/M]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO :(! Digite apenas M ou F.')

    dados['idade'] = int(input('Idade: '))  
    
    banco.append(dados.copy())
    id.append(dados['idade'])
    
    if dados['sexo'] in 'F':
        mulheres.append(dados['nomes'])

    while True:
        continuar = str(input('Você deseja continuar [S/N]? ')).upper()[0] 
       
        if continuar in 'SN':
            break
        print('ERRO :(! Digite apenas S ou N.')
    if continuar == 'N':
        break

media = sum(id) / len(banco)

print('=-='*30)
print(f'        A) Ao todo temos {len(banco)} pessoas cadastradas! ')
print(f'        B) A média de idade é {media}')

print(f'        C) As mulheres cadastradas foram {", ".join(mulheres)}!') #O join() junta os elementos de uma lista (ou qualquer iterável) em uma única string

print('Lista das pessoas cadastradas acima da média!')

for p in banco:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')