# TUPLAS = VÁRIAVEIS COMPOSTAS

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') 
# print(lanche[-1])''' 
 
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') 

for cont in range (0, len(lanche)): 
   print(f'Eu vou comer {lanche[cont]} na posição {cont}') # POR MEIO DESSE METODO PODEMOS DESCOBRIR A POSIÇÃO EM QUE O ITEM DA VARIAVEL ESTA 
 
for pos, comida in enumerate(lanche): 
  print(f'Eu vou comer {comida} na posição {pos}') 

for cont in range ( 0, len(lanche)): #O RANGE RECEBE A CONTAGEM DE 0 A 4 PQ DESCONSIDERA O 5, O LEN CONTA A QUANTIDADE DE ITENS NA VARAIVEL 
   print(lanche[cont]) # AQUI ENTÃO TEMOS QUE O LANCHE NA POSIÇÃO DE CONT, OU SEJA VAI APARECER O NOME DE CADA ITEM ASSIM 

for comida in (lanche): # ELE DA LOOP ATÉ ACABAR A VARIAVEL 
  print(f'Eu vou comer {comida}') 
  
print('Comi demais!') 

print(sorted(lanche)) # ORGANIZA A VARIAVEL LANCHE

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # ORDEM TEM DIFERENÇA
print(c)
print(len(c)) # QUANTOS NÚMEROS TEM
print(c.count(5)) #QUANTAD VEZES O 5 SE REPETE DENTRO DE C 
print(c.index(8)) # MOSTRA A POSIÇAO DO NÚMERO

pessoa = ('Arthur', 17, 'M', 88.99)
del(pessoa)
print(pessoa) # eu tenho a definição de pessoa porem logo a baixo eu apaguei ela, executando o comando DEL
