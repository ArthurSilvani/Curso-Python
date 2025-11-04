#AULA 13

'''for c in range(0,6): # REPETE O 'OI' 6 VEZES, E NO FIM DA FIM UMA VEZ
    print('oi')
print('FIM')'''

for c in range(0,6): #REPETE INTERCALDO
    print('oi')
    print('FIM')

for c in range(0,6): #O ULTIMO NUMERO ELE IGNORA, OU SEJA, POEM 1+
    print(c)

for c in range(0, 7, 2): # DE 0 ATÉ 6 PULANDO 2 CASAS POR VEZ
    print(c) 

for c in range(6,0, -1): # AQUI CONTA DO MAIOR PARA O MENOR - LEMBRAR DO -1
    print(c)

n = int(input('Digite um número: '))

for c in range(0, n+1):
    print(c)


i = int(input('Inicio: '))
f = int(input('fIm: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('FIM')

for c in range(0, 3):
    n = int(input('Digite seu nome: ')) #ISSO SE REPETIRÁ 3 VEZES.
print('burro')

s = 0

for c in range(0,3):
    n = int(input('Digite um numero: '))
    s += n
print(f'O valor final do somátorio é {s}. ')