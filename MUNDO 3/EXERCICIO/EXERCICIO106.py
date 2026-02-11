def texto(msg):

    print('\033[31m~]'*len(msg))
    print(msg)
    print('~' * len(msg))

#PROGRAMA PRINCIPAL
while True:
    titulo = '      \033[31mSISTEMA DE AJUDA PyHelp     '

    texto(titulo)

    prt = str(input('\033[mFunção ou Biblioteca >'))

    if prt.lower() == 'fim':
        print('ATÉ LOGO')
        break

    esc = f'        \033[1;32;40mAcessando o menu de comando {prt}'
    print('~'*len(esc))
    print(esc)
    print('\033[m~'*len(esc))
    help(prt)