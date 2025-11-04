#ESTRUTURA DE REPETIÇÃO WHILE:

'''for c in range(1,10): #AQUI EU SEI O LIMITE
    print(c)
print('FIM')'''

'''c = 1               #AQUI EU TBM SEI O LIMITE, PORÉM O WHILE POSSO USAR QUANDO NÃO SEI O LIMITE
while c < 10:
    print(c)
    c += 1
print('FIM')'''

'''for c in range(1,5):  #AQUI ESTOU DELIMITANDO O A QUANTIA DE VALORES QUE EU QUERO EM MEU PROGRAMA
    n = int(input('Digite um valor: '))
print('FIM')'''

''''n = 1 

while n != 0: #AQUI QUALQUER NUMERO DIFEENTE DE ZERO QUE FOR DIGITADO ELE IRA CONTINUAR PEDINDO O VALOR, SE DIGITAR 0 ELE PARA
    n = int(input('Digite um valor: '))
print('FIM')'''

# AQUI SE A RESPOSTA FOR 'SIM' ELE IRÁ LER NOVAMENTE, CASO TIVER UM NÃO CHEGARÁ AO FIM
'''r = 'S'

while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar?  [S/N]  ')).upper()
print('FIM')'''

n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1 
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números impares!')




'''par = 1
par = 1 + 1
par = 2
par = par + 1'''

        