#Reto: Validación de contraseña
#Hackeaste la contraseña del laboratorio secreto del villano.
# Escribe un programa que te permita verificar si una contraseña cumple con lo siguiente:
#* La contraseña debe tener al menos 8 caracteres.
#* La contraseña debe contener al menos una letra mayúscula y una letra minúscula.
#* La contraseña debe contener al menos un número.
#* La contraseña no debe contener espacios en blanco.


def characters_check(password: str):
    if len(password) >= 8:
        upper_check(password)
    else:
        print('No es una contraseña valida, tiene menos de 8 caracteres')


def upper_check(password: str):
    password_upper = [m for m in password if m == m.upper() and not m.isdigit()]
    password_lower = [m for m in password if m == m.lower()]
    if len(password_upper) > 0 and len(password_lower) > 0:
        number_check(password)
    else:
        print('La constraseña es invalida, no contiene al menos una letra mayuscula y una letra minúscula')


def number_check(password: str):
    password_number = [int(n) for n in password if n.isdigit()]
    if len(password_number) > 0:
        spaces_check(password)
    else:
        print('Contraseña invalida, no contiene al menos un número')


def spaces_check(password:str):
    if " " in password:
        print('Contraseña invalida, contiene espacios')
    else:
        print('Contraseña valida, cumple con todos los parámetros')


password = input('Ingresa la constraseña que robaste, para verificar: ')
characters_check(password)
