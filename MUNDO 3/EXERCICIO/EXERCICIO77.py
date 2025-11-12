#CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS (NÃO USAR ACENTOS).
#dEPOIS DISSO, VOCÊ DEVE MOSTRAR PARA CADA PALAVRA AS SUAS VOGAIS.     

palavras = ('programar','estudar','pensar','comprir','jogar','furia')

for p in palavras:  
    print(f'\nNa palavra {p.upper()} temos as vogais : ',end='') #AQUI EU QUEBREI E AJUSTEI EM UMA LINHA COM O END
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            
