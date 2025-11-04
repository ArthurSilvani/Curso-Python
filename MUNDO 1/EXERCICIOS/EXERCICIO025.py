#CRIE UM PROGRAM QUE LEIA O NOME DE UMA PESSOA E DIGA
#SE ELA TEM "SILVA" NO NOME

nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')