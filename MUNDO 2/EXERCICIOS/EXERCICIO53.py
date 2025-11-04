#CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM POLÍNDROMO,
# DESCONSIDERANDO OS ESPAÇOS. 

frase = str(input('Digite uma frase aqui: ')).strip().replace('',"").upper()

if frase[::] == frase[::-1]:
    print('a frase sugerida é um polimedro')
