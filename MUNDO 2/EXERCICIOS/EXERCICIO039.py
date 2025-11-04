from datetime import datetime

alistamento = int(input('Ano de nascimento: '))

idade = datetime.now().year - alistamento

passado = idade - 18

futuro = 18 - idade

print(f'Quem nasceu em {alistamento} tem em {datetime.now().year}, {idade} anos! ')
if idade > 18:
    print(f'Você deveria ter se alistado a {passado}!')
elif idade < 18:
    print(f'Você deverá esperar mais {futuro}, para se alistar no exercito. ')
else:
    print(f'Você tem {idade}, deve se alistar nesse ano. LEMBRE-SE!!')