
# Reto 1
#Mission Impossible: Beat the panther_Reto 1
# Eres un espía y acabas de extraer el número de tarjeta de crédito de María;
# necesitas verificar si el número de tarjeta de crédito es válido antes de
# realizar una transacción e infiltrarte en la mansión del villano.
# Escribe un programa que te permita validar números de tarjeta de crédito utilizando el algoritmo de Luhn.

# par->2 impar->1


def more_two_numbers(n):
    n = str(n)
    n_list = [int(number) for number in n]
    total = sum(n_list)
    return total


def verify_card(card):
    total = 0
    for n in range(len(card)):
        if n % 2 == 0:
            phase_1 = card[n] * 2
        else:
            phase_1 = card[n] * 1
        if phase_1 > 9:
            phase_1 = more_two_numbers(phase_1)
        total += phase_1
    if total % 10 == 0:
        print('Número de tarjeta valida, puede infiltrarse con tranquilidad 😎')
    else:
        print('Número de tarjeta invalido, corra por su vida 😫')


ok = True

while ok:
    try:
        credit_card = input('Ingresa el número de tarjeta de crédito: ')
        card_list = [int(n) for n in credit_card]
    except ValueError:
        card_list = 'Ingresa solo números'
        print(card_list)
    else:
        ok = False
        verify_card(card_list)


