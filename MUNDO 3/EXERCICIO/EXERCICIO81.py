#CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS DIGITADOS E COLOCAR EM UMA LISTA 
#DEPOIS DISSO, mostre:
# A - QUANTOS NÚMEROS FORAM DIGITADOS
# B - A LISTA DE VALORES ORDENADA DE FORMA DECRESCENTE
# C -  SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA 

valores = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    
    continuar = (input('Você deseja continuar [S/N]? ')).upper()

    valores.sort(reverse=True)

    if continuar == 'N':
        print(f'O número de valores digitados na lista é igual {len(valores)}')
        print(f'A Lista em ordem descrescente é assim {valores}!')
        
        if 5 not in valores:
            print('Não achei o número 5...')
        else:
            print('O número 5 se encontra na lista. :)')
        break
        