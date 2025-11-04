#FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA 
# PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIA DE TINTA NECESSÁRIA PARA
# PINTA-LÁ, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2M

l = float(input('A largura da sua parede: '))
a = float(input('Altura da sua parede '))
area = l * a 
print(f'Sua parede tem dimensão de {l} x {a} e a sua área é de {area:.2f}m')
tinta = area / 2
print(f'Para pintar sua parede, é necessário de {tinta:.2f}L')