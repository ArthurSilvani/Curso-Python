#FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VARIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VALOR
# DIGITADO PELO USUARIO. O PROGRAMA SERA INTERROMPIDO QUANDO O NUMERO SOLICITADO FOR NEGATIVO

n = 0

while True:
    n = int(input('Qual tabuada você deseja ver? '))
   
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    
    print('-'*30)

    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    
    print('-'*30)

    