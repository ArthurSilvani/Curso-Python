#CRIE UM PROGRAMA QUE LEIA VARIOS NÚMEROS INTEIROS PELO TECLADO. NO FINAL DA EXECUÇÃo, MOSTRE A MÉDIA ENTRE TODOS OS VALORES E 
#QAUL FOI O MAIOR E O MENOR VALORES LIDOS. O PROGRAMA DEVE PERGUNTAR AO USUARIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES
cont = media = maior = menor = cmedia = 0
resp = 'Ss'
while resp == 'Ss':
        número = int(input('Digite um número: '))
        continuar = str(input('Quer continuar [S/N]: ')).upper()
        cont += 1 
        media += número
        cmedia = media / cont
        
        if cont == 1:          # CALCULO DE MAIOR E MENOR, SE EU FALAR 5, ELE É O MAIOR E O MENOR aula 14
              maior = número
              menor = número
        elif número > maior:
              maior = número
        elif número < menor:
              menor = número
        
        if continuar in 'Nn':
            print(f' A quantidade de números digitados por você foi {cont}, com {cmedia} de media. ')
            print(f' O {maior} foi o maior valor digitado e o {menor} foi o menor valor. ')
         


