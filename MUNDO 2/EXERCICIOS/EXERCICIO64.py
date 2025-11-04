#crie um programa que leia varios números inteiros pelo teclado. O programa so vai parar
#quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos numeros
# foram digitados e qual foi a soma entre eles( desconsiderando o FLAG 999)

n = cont = soma = 0

while n != 999:
     
     n = int(input('Digite qualquer valor [ 999 para parar ]? '))
     
     soma += n
    
     if n != 999:
         cont += 1
    
          
print(f'Você digitou {cont} números, seus numeros somados da: {soma-999}.')

    