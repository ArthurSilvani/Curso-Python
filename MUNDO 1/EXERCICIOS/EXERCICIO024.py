#crie um programa que leia o nome de uma cidade
#e diga se la começa ou não com o nome "SANTO"

cid = str(input('Digite o nome da sua cidade: ')).strip()

print(f'{"SANTO" in cid.upper()}')