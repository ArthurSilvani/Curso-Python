#FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DA PESSOA
#MOSTRANDO EM SEGUIDA O PRIMEIRO E O ULTIMO NOME SEPARADAMENTE

nome = str(input('Digite seu nome completo: ')).strip().split()

print(f'Muito prazer em te conhecer!')

print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu ultimo nome é: {nome[len(nome)-1]}')