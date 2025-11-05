# CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA COM UMA CONTAGEM POR EXTENSO, DE ZERO ATÉ VINTE.
# SEU PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO (ENTRE 0 E 20) E MOSTRÁ-LO POR EXTENSO

contagem = ( 'zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito',
            'nove', 'dez', 'onze', 'doze',
            'treze', 'quatorze', 'quinze', 'dezeseis',
            'dezesete', 'dezoito', 'dezenove', 'vinte' )
while True:
    pergunta = int(input('Digite um número entre 0 e 20: '))
    if 0 <= pergunta <= 20:
        break
    print('Tente novamente. Digite um número entre 0 e 20.')
    
print(f' Você digitou o número {contagem[pergunta]}')

