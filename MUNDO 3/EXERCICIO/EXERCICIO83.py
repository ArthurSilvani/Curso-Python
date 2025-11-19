#CRIE UM PROGRAMA ONDE O USUARIO DIGITE UMA EXPRESSÃO QUALQUER QUE USE PARÊNTESES.
#SEU APLICATIVO DEVERÁ ANALISAR SE A EXPRESSÃO PASSADA ESTÁ COM O PARÊNTESES ABERTOS E FECHADOS NA ORDEM CORRETA

expr = str(input('Digite a expressão: '))

if expr.count('(') == expr.count(')'):
    print('Sua expressão é válida!!')
else:
    print('Sua expressão não é válida')
