#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

#Quantidade de notas
#A maior nota
#A menor nota
#A média da turma
#A situação (opcional)

# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

#Programa principal

def notas(*valores, sit=False):
    
    tot = len(valores)
    soma = 0
    maior = menor = valores[0]
    
    for v in valores:
        soma += v
        if v > maior:
            maior = v
        elif v < menor:
            menor = v
  
    if soma > 7:
        sit = 'Boa'
    elif 5 < soma > 7:
        sit = 'Razoavel'
    else:
        sit = 'Ruim'
    
    valores = {'total': tot, 'Média': soma, 'Maior:': maior, 'Menor:': menor, 'situação': sit }
    return valores

resp = notas(1.0, 3.6, 2)

print(resp)

