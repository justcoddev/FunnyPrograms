import random

nombres = ['Cristina', 'Lisseth', 'Karla', 'Nicole', 'Dennisse',
           'Camila', 'Paul', 'Carlos', 'Raul', 'Cristhian', 'Alejando']


def combinador(nombres):
    aleatorio1 = random.randint(0, len(nombres)-1)
    aleatorio2 = random.randint(0, len(nombres)-1)
    return nombres[aleatorio1] + ' ' + nombres[aleatorio2]


while True:
    print('Generador de nombres:  \n')
    print(combinador(nombres))
    opt = input('Quiere ver otro nombre s/n :')
    if opt == 'n' or opt == 'N':
        break
