#DICIONARIOS

'''pessoas = {'nome': 'Arthur', 'sexo': 'M', 'idade': '22'}
print(pessoas)
print(pessoas['nome'])

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos! ') #QUANDO TRATARMOS OS DICIONARIOS DEVE-SE USAR DUAS ASPAS

print(pessoas.values()) #AQUI MOSTRA OS VALORES DOS DADOS ARMAZENADOS, QUE SÃO ELES (Arthur, M, 22)

print(pessoas.keys()) # AQUI SERÁ MOSTRADO OS INDICADORES DOS VALORES, QUE SÃO ELES (Nome, Sexo, Idade)

print(pessoas.items()) # AQUI IRÁ MOSTRAR OS DOIS, TANTO VALOR QUANTO OS INDICADORES

del pessoas['sexo'] # EXCLUI 

pessoas['peso'] = '90.6' # ADICIONA NO DICIONARIO

for k, v in pessoas.items(): # PARA CADA KEYS E VALORES EM PESSOAS.ITEMS()
    print(f'{k} = {v}')'''

#---------------------------------------------------------------------------------------------------------------------------------------]

'''brasil = list()

estado1 = { 'uf': 'Rio Grande do Sul', 'sigla': 'RS'}
estado2 = { 'uf': 'Santa Catarina', 'sigla': 'SC'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil) #MOSTRARA OS DOIS ESTADOS ADICIONADOS NA LISTA
print(brasil[0]) #MOSTRA O PRIMEIRO ESTADO, OU SEJA, RIO GRANDE DO SUL
print(brasil[1]) #MOSTRARÁ O SEGUNDO ESTADO, OU SEJA, SANTA CATARINA 

print(brasil[0]['uf'])''' # O '0' IDENTIFICA O VALOR DA LISTA QUE IRA MOSTRAR JÁ O 'UF' É O INDICADOR DO VALOR QUE ESTA NO PRIMEIRO ESTADO ADICIONADO NO DICIONARIO

#---------------------------------------------------------------------------------------------------------------------------------------

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())

print(brasil)

for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}', end=' ') 
    print()

