#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO. 
#SE ELE ULTRAPASSAR 80KM/H MOSTRE UMA MENSAGEM DIZENDO QUE ELE 
#FOI MULTADO. A MULTA VAI CUSTAR R$ 7.00 POR CADA KM ACIMA DO LIMITE

print(' -=- '* 10)
print('-RADAR ELETRONICO-')
print(' -=- '* 10)

vl = int(input('Qual é a velocidade atual do carro? '))

multa = (vl-80) * 7

if vl < 80:
    print('Tenha um Bom dia! Dirija com segurança.')
print(f'MULTADO! A sua multa será no valor de R$ {multa:.2f}.Tome mais cuidado!')