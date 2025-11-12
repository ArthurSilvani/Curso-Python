#CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS NA SEQUENCIA 
#NO FINAL, MOSTRE UMA LISTAGEM DE PREÇOS, ORGANIZANDO OS DADOS EM FORMA TABULAR

nome_produtos = ('caneta', 'borracha', 'caderno', 'estojo', 'mochila')
preco_produtos = (1.50, 1, 25, 15, 100)
f = ('.'*30)
for contator in range(0, len(nome_produtos)):
    print(f'{nome_produtos[contator]}{f}R${preco_produtos[contator]}')

