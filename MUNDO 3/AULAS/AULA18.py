#AULA 18 - LISTAS (PARTE 2)

'''teste = list() #CRIE UMA LISTA

teste.append('Arthur') #ADICIONEI ELEMENTOS EM MINHA LISTA
teste.append(17)

galera = list()
galera.append(teste[:]) # COLOQUEI MINHA LISTA DENTRO DE OUTRA LISTA

teste[0] = 'Amanda'
teste[1] = 18 #ADICIONEI MAIS COISAS NA MINHA LISTA, AQUI FEZ UMA LIGAÇÃO COM A PRIMEIRA LISTA CRIADA NO INCIO

galera.append(teste[:])

 #AQUI OS DOIS SE LIGARAM, ELES SE MUDAM OS DOIS, RECISO FAZER UMA COPIA

galera.append(teste[:]) # ESSE É O COMANDO PARA REALIZAR A COPIA

print(galera)'''

''''galera = [['João', 13], ['Arthur', 17], ['Ursula', 22], ['Patolino', 90]]

print(galera) #APARECE TODOs
print(galera[0]) # SO APARECE ['JOÃO', 13] POR SER O 0 DA MAIOR LISTA
print(galera[0][1]) # APARECE O APENAS O ['JOÃO'] QUE É O PRIMEIRO ITEM

for p in galera:
    print(p) #FAZ UMA LISTA
    print(p[0]) #LISTA SO DOS NOMES
    print(f'{p[0]} tem {p[1]} anos')'''

galera = list()
dado = list()

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
    else:
        print(f' {p[0]} é menor de idade')