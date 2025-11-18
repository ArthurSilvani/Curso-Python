# AULA 17 - LISTAS (PARTE 1)

num = [1, 2, 3, 4, 5]

num[2] = 8 #AQUI NAS LISTAS ELAS SÃO MUTAVEIS, OU SEJA TRANSFORMEI O NUMERO QUE ESTAVA NA POSIÇÃO 2, QUE É O N3, para o numero 8 

num.append(9) # ADICIONO UM NÚMERO A LISTA

num.sort() # deixa os a lista em ordem 

num.sort(reverse=True) # DEIXA DO MAIOR PARA O MENOR, OU SEJA AO CONTRARIO - A ORDEM 

num.insert(2, 2) # AQUI ESTOU INSERINDO O NUMERO 7 NA POSIÇÃO DOIS USANDO INSERT

num.pop() # O POP ELIMINA O ULTIMO ELEMENTO DE UMA LISTA, POREM SE COLOCARMOS A POSIÇÃO QUE GOSTARIAMOS DE ELIMINAR ELE TAMBEM SERVE COMO ESSA FUNÇÃO

if 9 in num:
    num.remove(9) # O REMOVE ELE PROCURA O PRIMEIRO ELEMENTO QUE MANDEI REMOVER, MESMO QE ESTES ESTEJAM REPETIDOS NA LISTA
else:
    print('Não achei o número 3')

print(num)

print(f'Essa lista tem {len(num)} elementos.') # CONTA QAUNTOS NUMEROS TEM NA LISTA


valores = []

valores.append(9)
valores.append(0)
valores.append(2)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!') # SE EU QUISESSE TUDO EM UMA LINHA SO DAR END=''
print('Cheguei ao final!')

valores = list()

for cont in range(0,5):
    valores.append(int(input('Digite um valor: '))) # AQUI HÁ UMA LEITURA DO TECLADO DO USUARIO, ELE IRÁ POR 5 NUMEROS POIS É ISSO QUE O FOR FEZ 

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!') # SE EU QUISESSE TUDO EM UMA LINHA SO DAR END=''
print('Cheguei ao final!')

a = [2,5,6,7]
b = a[:]    # COM AS CHAVES E OS DOIS PONTOS, CRIA-SE ENTÃO UMA COPIA E NÃO UMA LIGAÇÃO

b[2] = 8 # APARTIR DO MOMENTO EM QUE EU IGUALO UMA LISTA A OUTRA O PYTHON FAZ UMA LIGAÇÃO ENTRE ELAS
# NA LINHA A CIMA TEMOS QUE NA LISTA B QUE É IGUAL A 'A' O ELEMENTO QUE ESTA NA POSIÇÃO 2 VIRE O 8, POREM ASSIM SE ALTERÁ NAS DUAS LISTAS POR SEREM IGUAIS E FAZEREM LIGAÇÃO

print(f'Lista A: {a}')
print(f'Lista B: {b}')
    


