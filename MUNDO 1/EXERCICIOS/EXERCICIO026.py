#FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
#1-QUANTAS VEZES APARECE A LETRA 'A'
#2-EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
#3-EM QUE POSIÇÃO ELA PARECE A ULTIMA VEZ

let = str(input('Digite uma frase qualquer: ')).upper().strip()

l = let.count("A")
print(f'A letra A aparece {l} vezes na frase')
print(f'A primeira letra A aparece na posição {let.find("A")+1}')
print(f'A ultima letra A aparece na posição: {let.rfind("A")+1}')