letras = 'abcdefghijklmnopqrstuvwxyz'

# TODO: funcion de cifrado


def cifrar(text):
    temp = ' '
    numIndex = 0
    for letra in text:
        if letra in letras:
            numIndex = letras.find(letra) + 13
            
            if numIndex > len(letras):
                numIndex = numIndex - len(letras)
            elif numIndex < 0:
                numIndex = numIndex + len(letras)
            temp += letras[numIndex]
        else:
            temp += letra
    return temp

# TODO: funcion de descifrar


def descifrar(text):
    temp = ' '
    numIndex = 0
    for letra in text:
        if letra in letras:
            numIndex = letras.find(letra) - 13
            if numIndex < 0:
                numIndex = numIndex + len(letras)
            temp += letras[numIndex]
        else:
            temp += letra
    return temp


# TODO: funcion principal



def main():
    text = ''
    while True:
        print('Bienvenidos a cifrador rot13')
        msg = input('Ingrese el texto: ')
        opt = input('seleccione c(cifrar) d(descifrar)')

        if text.upper() == 'QUIT':
            break
        
        if opt.startswith('c'):
            text = cifrar(msg)
        elif opt.startswith('d'):
            text = descifrar(msg)
        else:
            print('Valor no valido')
            text = ''
        print('\n')
        print(text)
        print('\n')


main()
