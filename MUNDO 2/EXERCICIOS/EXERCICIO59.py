#CRIE  UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU COMO O AO LADO DA TELA:
#SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

opção = 0

while opção != 5: 
    print('='*30)
    print('''    \033[31m[1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA\033[m''')
    
    opção = int(input('\033[34m----> QUAL SUA ESCOLHA? \033[m'))
    
    if opção == 1:
        print(f'A soma desses dois números é = {n1+n2}! ')
    
    elif opção == 2:
        print(f'A multiplicação desses dois números é = {n1*n2}! ')
    
    elif opção == 3:
        if n1 == n2:
            print('Esses valores digitados são iguais...')
        elif n1 > n2:
            print(f'O maior valor digitado é {n1}. ')
        else:
            print(f'O maior valor digitado é {n2}. ')
    
    elif opção == 4:
        print('Informe novamente os números aqui:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))

    elif opção == 5:
        print('Você desejou sair do programa...')
    
    else:
        print('A sua escolha não se encaixa nas normas. Tente novamente ---> ')

