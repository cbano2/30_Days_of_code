# Dificultad difícil
# El adivinador de números
#
# Historia: Eres un adivinador profesional que ha sido desafiado a adivinar un número secreto. Tienes un máximo de 5 intentos para adivinar el número correcto. Después de cada intento, recibirás una pista para ayudarte a acercarte al número secreto.
#
# Instrucciones:
#
# 1. Escribe un programa en Java que genere un número aleatorio entre 1 y 100 como el número secreto.
# 2. Pídele al usuario que ingrese un número como su intento.
# 3. Compara el número ingresado con el número secreto y muestra un mensaje indicando si el número ingresado es mayor, menor o igual al número secreto.
# 4. Repite los pasos 2 y 3 hasta que el usuario adivine el número secreto o se queden sin intentos.

import random as r


def generate_number() -> int:
    return r.randint(1, 100)


guess = True
random_number = generate_number()
attempts = int(input('Ingresa el número de intentos que deseas tener : '))
while guess:
    if attempts != 0:
        number_user = int(input('Ingrese un número: '))
    if number_user == random_number and attempts != 0:
        print('Felicitacions 😎, has adivinado el numero secreto')
        guess = False
    elif number_user > random_number and attempts != 0:
        print('Te has pasado un poquito 😮, tu número es mayor al numero secreto')
        attempts -= 1
    elif number_user < random_number:
        print('Te quedaste corto 😥, tu número es menor al número secreto')
        attempts -= 1
    elif attempts == 0:
        print('Lástima 😫, te quedaste sin intentos. Mejor suerte para la próxima')
        print(f'El número secreto era: {random_number}')
        guess = False