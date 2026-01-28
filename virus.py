import os 

os.system("cls")
os.system("color 4")

print(' Vírus detectado! :(')

senha = input('Digite a senha correta: ')

if senha != "amandalinda":
    os.system("shutdown /s /t 1")
else:
    print('Vírus removido com sucesso! :)')