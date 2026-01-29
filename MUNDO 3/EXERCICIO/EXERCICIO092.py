#crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os ( com idade) em um dicionario
#se por acaso a CTPS for diferente de 0, o dicionarioi recebera tambem o ano de contratação e o salario. Calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar
from datetime import datetime
dados = dict()

dados['nome'] = str(input('Nome do funcionário: '))
nsc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nsc
dados['ct'] = str(input('Carteira de trabalho (0 se não tiver): '))

if dados['ct'] != '0':
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 65 ) - datetime.now().year 

for k, v in dados.items():
    if dados['ct'] != '0':
        print(f'    -{k} tem valor {v}')
    print(f'    -{k} tem valor {v}')
    

     

