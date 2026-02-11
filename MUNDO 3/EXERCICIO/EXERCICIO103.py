def ficha(nome = '<desconhecido>', gols = 0):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    
    return f'O jogador é {nome} e ele tem {gols} gols!'
    
a = input('Nome do jogador: ')
b = input('Quantos gols: ')
print(ficha(a,b))