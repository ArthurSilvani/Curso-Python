#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
#  só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')

def leiaInt(n):
     while True:   
        n = input('Digite um número: ')
        if n.isdigit():
            return n
        else:
            print('\033[4;31mErro! Digite Novamente. Burro!\033[m')


#Programa principal

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}!')
