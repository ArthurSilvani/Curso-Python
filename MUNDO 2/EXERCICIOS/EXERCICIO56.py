#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa mostre:
#A MÉDIA DE IDADE DO GRUPO
#QUAL O NOME DO HOMEM MAIS VELHO
#QUANTAS MULHERES TÊM MENOS DE 20 ANOS

menor = 0
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho ='' 

for analisador in range(1, 5):
    print('-------- {analisador} --------')
 #QUESTOES   
    no = input('Nome: ')
    id = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).upper()
#HOMEM
    if analisador == 1 and sex == 'M':
        maioridadehomem = id
        nomevelho = no
    if sex == 'M' and id > maioridadehomem:
        maioridadehomem = id
        nomevelho = no
#IDADE
    somaidade += id #ESSA SOMA RECEBE A IDADE DA PESSA
    mediaidade = somaidade / 4
#MULHER
    if sex == 'F':
      if id < 20:
        menor += 1

print(f'A MÉDIA DE IDADE DO GRUPO É DE {mediaidade}.')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'Ao todo são {menor} mulheres com menos de 20 anos.')