#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
#Aproveite e crie também uma função leiaFloat()com a mesma funcionalidade.

def leiaInt(msg):
     while True:
            try: 
                n = int(input(msg))
            except (ValueError, TypeError):
                print('ERRO. Coloque um numero valido!')
                continue
            else: 
                return n

def leiaFloat(via):
     while True:
        try:
            g = float(input(via))
        except (ValueError, TypeError):
            print('ERRO. Coloque um numero valido!')
            continue
        else: 
            return g
        
        

#Programa principal

num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}!')