#FAÇA UM PROGRMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS
#DIGITOS SEPARADOS 

#num = int(input('Digite um número: '))

#n = str(num)

#print(f'Unidade: {n[3]}')
#print(f'Dezena: {n[2]}')
#print(f'Centena: {n[1]}')
#print(f'Milhar: {n[0]}')

nume = int(input('Digite um número: '))

u = nume // 1 % 10
d = nume // 10 % 10
c = nume // 100 % 10
m = nume // 1000 % 1000

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

