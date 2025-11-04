# DESENVOLVA UMA LOGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA,
# CALCULE SEU IMC E MOSTRE SEU STATUS, DE ACORDO COM a TABELA ABAIX0:
# ABAIXO DE 18.5: ABAIXO DO PESO
# ENTRE 18.5 E 25: PESO IDEAL
# 25 ATÉ 30: SOBREPESO
#30 ATÉ 40: OBESIDADE
# ACIMA DE 40: OBESIDADE MORBIDADE

peso = float(input('Qual é o seu peso? KG '))
altura = float(input('Qual a sua altura? CM '))

imc = peso / ( altura * altura)

print(f'A média do seu peso é {imc:.0f}KG')

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc > 18.5 and imc < 25:
    print('PESO IDEAL')
elif imc > 25 and imc < 30:
    print('SOBREPESO')
elif imc > 30 and imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')

