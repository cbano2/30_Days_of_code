# Reto 3 (Número mágico)

def odd_validator(number: int):
    if number % 2 != 0:
        return True
    else:
        return False


def divisibility_3(number: int):
    if number % 3 == 0:
        return True
    else:
        return False


def addition_number(number: int):
    number_list = [int(n) for n in str(number)]
    total = sum(number_list)
    if total == 7:
        return True
    else:
        return False


lower = int(input("Ingresa el límite inferior: "))
upper = int(input("Ingresa el límite superior: "))


magic_number = [m for m in range(lower, upper+1) if odd_validator(m) and divisibility_3(m) and addition_number(m)]
if len(magic_number) > 0:
    print(magic_number)
else:
    print('No hay número mágico 😥')

