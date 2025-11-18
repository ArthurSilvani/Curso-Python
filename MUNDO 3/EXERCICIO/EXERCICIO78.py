# FAÇA UM PROGRAMA QUE LEIA 5 VALORES NÚMERICOS E GUARDE-OS EM UMA LISTA.
# NO FINAL, MOSTRE QUAL FOI O MAIOR VALOR E O MENOR VALOR DIGITADO E AS SUAS RESPECTIVAS POSIÇOES NA LISTA 

valores = list ()
p_maior = []
p_menor = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para o posição {cont}: ')))

print('--'*25)
print(f'Os valores da sua lista são {valores}!')
for p, v in enumerate(valores):
    if v == max(valores):
       p_maior.append(p)
    elif v == min(valores):
        p_menor.append(v)

print(f'O maior numero digitado é {max(valores)} e está na posição {p_maior}  ')

print(f'O menor numero digitado é {min(valores)} e está na posição {p_menor}  ')


