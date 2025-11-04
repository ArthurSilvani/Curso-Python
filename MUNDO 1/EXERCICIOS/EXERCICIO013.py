#FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONARIO E MOSTRE 
#SEU NOVO SALÁRIO, COM 15% DE AUMENTO.

s = float(input('Qual o salário atual do Funcionário? R$ '))

amt = s + (s * 15 / 100)

print(f'O Funcionario que recebia R${s}, com aumento de 15%, passará a receber R${amt:.2f} !!')
