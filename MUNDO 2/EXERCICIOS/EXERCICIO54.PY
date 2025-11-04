#CRIE UM PROGRAMA QUE LEIA O ANO DE SETE PESSOAS.
#NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES
from datetime import date

atual = date.today().year #PEGAR ANO ATUAL DO PC

totmaior = 0 
totmanor = 0

for c in range(1, 8):
    nsc = int(input(f'Em que ano {c} nasceu? '))

    idade = atual - nsc

    if idade >= 21:
        totmaior += 1 #SE TIVER UMA PESSOA MAIOR, ESSA FUNÇÃO ADD MAIS UMA PESSOA
    else:
        totmanor += 1
print(f'Ao todo tivemos {totmaior} maiores de idade.')
print(f'E {totmanor} menores de idade.')
