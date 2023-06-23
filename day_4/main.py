#Descripción del desafío:

#El programador debe ingeniar una manera de ingresar una pareja de límites (inferior y superior).
#Debe ser capaz de manejar varios casos que consisten en parejas de límites. (ejemplo 1-10,20-30,...)
#Para cada caso, el programa debe encontrar y sumar todos los números pares dentro del rango especificado.
#El programa debe mostrar en pantalla la suma de los números pares obtenida para cada caso.

def is_pair(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False


def total_pair(list_int: list) -> int:
    total = 0
    for n in list_int:
        if is_pair(n):
            total += n
    return total


limit = input('Ingresa tus límites en el siguiente formato (li-ls): ')
limit_list = limit.split('-')
limit_list_int = [n for n in range(int(limit_list[0]), int(limit_list[1])+1)]
print(f'El total es: {total_pair(limit_list_int)}')