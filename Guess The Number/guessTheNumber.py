import random
import os


def guess():
    print('\tBienvenido')
    print('\t   a')
    print('\tADIVINA EL NUMERO')
    nombre = input('Cual es tu nombre: ')
    print(f'Oye {nombre} estoy pensando un numero entre 1 a 20 ')
    intentos = 0
    numero = random.randint(1, 20)
    
    while intentos < 6:
        posible = int(input('Adivina el numero: '))
        intentos += 1
        if posible > numero:
            print('Está por abajo')
        elif posible < numero:
            print('Está por arriba')
        elif posible == numero:
            break
    if posible == numero:
        if intentos == 1:
            print(f'{nombre} has ganado en el primer intento')
            print('Es tu dia de suerte!')
        else:
            print(f'{nombre} has ganado en {intentos} intentos')
            print('Bien hecho...')
    else:
        print(
            f' {nombre} tenias {intentos} intentos, el numero era {numero}')
        print('Mas suerte en la proxima...')


def guess_en():
    from googletrans import Translator
    translator = Translator()
    print('\tWelcome')
    print('\t   to')
    print('\tGUESS THE NUMBER')
    name = translator.translate('Cual es tu nombre: ')
    nombre = input(name.text)
    text1 = f'Oye {nombre} estoy pensando un numero entre 1 a 20 '
    text1_en = translator.translate(text1, dest='en')
    print(text1_en.text)
    intentos = 0
    numero = random.randint(1, 20)
    
    while intentos < 6:
        posible = translator.translate('Adivina el numero: ')
        posible_en = int(input(posible.text))
        intentos += 1
        if posible_en > numero:
            text2 = 'Está por abajo'
            text2_en = translator.translate(text2, dest='en')
            print(text2_en.text)
        elif posible_en < numero:
            text3 = 'Está por arriba'
            text3_en = translator.translate(text3, dest='en')
            print(text3_en.text)
        elif posible_en == numero:
            break
    if posible_en == numero:
        if intentos == 1:
            text4 = f'{nombre} has ganado en el primer intento\nEs tu dia de suerte!'
            text4_en = translator.translate(text4, dest='en')
            print(text4_en.text)

        else:
            text4 = f'{nombre} has ganado en {intentos} intentos\nBien hecho...'
            text4_en = translator.translate(text4, dest='en')
            print(text4_en.text)

    else:
        text4 = f' {nombre} tenias {intentos} intentos, el numero era {numero}\nMas suerte en la proxima...'
        text4_en = translator.translate(text4, dest='en')
        print(text4_en.text)


language = int(input('Language:\n\t1.Spanish\n\t2.English\n\t'))
if language == 1:
    os.system("cls")
    guess()
else:
    os.system("cls")
    guess_en()
