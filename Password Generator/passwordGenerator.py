import random

caracteres = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+~'


def password_generator(longitud=8):
    if longitud >= 8:
        num = 0
        temp = ''
        long_car = len(caracteres)
        while num < longitud:
            aleatorio = random.randint(0, long_car)
            temp += caracteres[aleatorio]
            num += 1
        return temp
    else:
        return 'Minimo una longitud de 8'

print('Bievenidos al generador de password seguro ')
longitud = int(input('Ingrese la longitud que quiera su password: '))
print('Su password generaa es:\n')
print(password_generator(longitud))