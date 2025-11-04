#FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SO ACEITE OS VALORES:
# 'M' E 'F'. CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO.

sexo = str(input('Informe seu sexo: [F/M] ')).upper()

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Qual seu sexo? [F/M] ')).upper()

print(f'O sexo informado pelo cliente é = {sexo} !')


