#escreva um programa que leia um valor em metros 
# e o exiba convertido em CM e MM

x = float(input('Uma distância em metros: '))
cm = x * 100
mm = x * 1000
print(f'Em CM esse valor é = {cm}' )
print(f'Em MM esse valor é = {mm:.0f}')

