#DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRES RETAS
#E DIGA AO USUARIO SE ELAS PODEM OU NÃO FORMAR UM TRIANGULO

print('-=-'*10)
print(' \033[0;30;41mANALISE ESTE TRIANGULO \033[m')
print('-=-'*10)

a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))

if a + b > c and a + c > b and b + c > a:
    print('Os segmentos ACIMA podem formar um triangulo.')
else:
    print('Os segmentos ACIMA NÃO podem formar um triangulo.')