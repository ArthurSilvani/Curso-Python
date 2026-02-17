#TRATANDO DE ERROS E EXCEÇOES

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))

    r = a / b
except:
    print('Infelizmente não deu certo :(')
else:
    print(f'O valor deu certo e é {r}   !')
finally:
    print('Volte sempre!')
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))

    r = a / b
except Exception as erro: # Awui para descobrir e descrever os erros que aconteceram
    print(f'Problema encontrado foi {erro.__cause__}')
else:
    print(f'O valor deu certo e é {r}   !')
finally:
    print('Volte sempre!')

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))

    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não e possivel dividir um numero por zero')
else:
    print(f'O valor deu certo e é {r}   !')
finally:
    print('Volte sempre!')


