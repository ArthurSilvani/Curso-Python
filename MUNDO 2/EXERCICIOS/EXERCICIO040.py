
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media =  (n1 + n2) / 2

if media >= 7.0:
    print(f'Você foi APROVADO, com {media} de média!')
elif media < 5:
    print(f'Você foi REPROVADO, com {media} de média. Deve se esforçar mais!')
elif media >= 5 and media < 7:
    print(f'Você pegou RECUPERAÇÃO, com {media} de média!')