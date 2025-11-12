#DESENVOLVA UM PROGRAMA QUE LEIA 4 VALORES PELO TECLADO E GUARDE0S EM UMA TUPLA. NO FINAL MOSTRE;
# A- Quantas vezes apareceu o valor 9. 
# B- Em que posição foi digitado o primeiro valor 3
# c- Quais foram os números pares. 

valores = ( int(input('Digite um número: ')),
            int(input('Digite um número: ')),
            int(input('Digite um número: ')),
            int(input('Digite um número: ')))
         
print(f'Você digitou os seguintes valores --> {valores}.')

print(f'O número nove se repetiu {valores.count(9)} vezes.') #CONTANDO A QUANTIDADE DE NÚMEROS, OU LETRA QUE HÁ NESSA TUPLA

if 3 in valores:
    print(f'O número 3 apareceu na {valores.index(3)+1}ª posição.')
else:
    print('O número 3 não foi digitado neste programa.')

print(f'Os números pares digitados são', end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')

