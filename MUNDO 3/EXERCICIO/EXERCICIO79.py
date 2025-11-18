#CRIE UM PROGRAMA ONDE O USÚARIO POSSA DIGITAR VÁRIOS VALORES NÚMERICOS E CADASTRE-OS EM UMA LISTA.
#CASO O NÚMERO JÁ EXISTA LÁ DENTRO, ELE NÃO SERÁ ADICIONADO. NO FINAL, SERÃO EXIBIDOS TODOS OS VALORES ÚNICOS DIGITADOS, EM ORDEM CRESCENTE

valor = list()

while True: 
    num = (int(input('Digite um valor: ')))

    if num not in valor:
        valor.append(num)
    elif num in valor:
        print('Valor duplicado... não adicionaremos a lista')
    
    continuar = (input('Você deseja continuar [S/N]: ')).upper()
    valor.sort()
    if continuar == 'N':
        print(f'Os valores digitados pelo usúario na lista são estes {valor}!')
        break
    