#DESENVOLVA UM PROGRMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM
#EM KM. CALCULE O PREÇO DA PASSAGEM, COBRANDO R$ 0,50 POR KM PARA VIAGENS
#DE ATE 200KM E R$ 0,45 PARA VIAGENS MAIS LONGAS

distancia = float(input('Digite qual a distância: '))

if distancia <=200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print(f'Você rodou {distancia}KM, o total a pagar será de R${valor}')


