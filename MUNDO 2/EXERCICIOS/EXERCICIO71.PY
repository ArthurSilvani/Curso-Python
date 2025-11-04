#CRIE UM PROFRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNIC. NO INICIO, PERGUNTE
# AO USUARIO QUAL SERÁ O VALOR A SER SACADO (NÚMERO INTEIRO) E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES
while True:
    print('-'*30)
    print('{:^30}'.format ('BANCO SICREDI'))
    print('-'*30)

    valor = int(input('Qual o valor de saque? '))
    if valor <= 1000000:
        milhar = (valor // 100)  % 200
        centena = ( valor // 100 ) % 10
        dezena = (valor // 10 ) % 10
        unidade = valor % 10
        print(f'Total de {milhar} cédula de R$ 200,00')
        print(f'Total de {centena} cédula de R$ 100,00')
        print(f'total de {dezena} cédula de R$ 10,00')
        print(f'Total de {unidade} cédula de R$ 1,00')
        break
   
