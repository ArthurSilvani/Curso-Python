#ESCREVA UM PROGRAMA QUE PERGUNTE O SALARIO DE UM FUNCIONARIO E CALCULE
#O VALOR DE SEU AUMENTO.
#PARA SALARIOS SUPERIORES A 1250, CALCULE UM AUMENTO DE 10%
#PARA OS INFERIORES OU IGUAL, O AUMENTO É DE 15%

'''salário = int(input('Qual é o salário do funcionário? R$ '))

maior = salário * ( 10 / 100) + salário
menor = salário * ( 15 / 100) + salário

if maior >= 1250:
    print(f'Quem ganhava R${salário}, passará a ganhar R${maior}')
else:
    print(f'Quem ganhava R${salário}, passará ganhar R${menor}')'''

#VERSÃO DO VÍDEO

salário = float(input('Qual é o salário do funcionário? R$ '))

if salário >= 1250: #MAIOR
    novo = salário + ( salário * 10 / 100)
else:
    novo = salário + ( salário * 15 / 100)
print(f'Quem ganhava R${salário:.2f}, passará a receber R${novo:.2f} agora. ')

