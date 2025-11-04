#DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E  MOSTRE A SOMA
# APENAS DAQUELES QUE FOREM PARES. SE O VALOR DIGITADO FOR IMPAR DESCONSIDEREO

soma = 0
for c in range(1, 7): # REPETE O 'NUM' 6VEZES
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num 
print(f'Você deu SEIS números a soma deles é igual a {soma}.')