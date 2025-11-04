# CONDICIONAIS ALINHADAS

nome = str(input('Qual é o seu nome? '))

if nome == 'Arthur':
    print('Nossa, que nome bonito!')
elif nome == 'Amanda' or nome == 'Ivanete'or nome == 'Jandir':
    print('Esse nome é bem conhecido!')
elif nome in ('Ana Claudia Jéssica Bela'):
    print('Que belo nome')
else:
    print('Seu nome é bem normal')
print(f'Tenha um bom dia, {nome}!')

