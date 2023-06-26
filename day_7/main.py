# Medianamente complejo: Validar una dirección de correo electrónico
# Desafío: Crea una función que verifique si una cadena dada representa
# una dirección de correo electrónico válida. La dirección de correo
# electrónico debe tener el formato "nombre@dominio.extension" y cumplir
#  con algunas reglas básicas, como tener al menos un carácter antes y
# después del símbolo "@".


def email_check(email: str):
    email_list = [c for c in email]
    if '@' in email_list:
        if len(email_list[:email_list.index('@')]) > 0:
            if len(email_list[email_list.index('@')+1:]) > 0:
                domain = email_list[email_list.index('@')+1:]
                if '.' in domain:
                    print('El email es valido')
                else:
                    print('El email no contiene un "." después del doniminio, invalido')
            else:
                print('No contiene un dominio, email invalido')
        else:
            print('No contiene un nombre, email invalido')

    else:
        'No contiene @ su email, no es valido'


email = input('Ingrese el email a verificar: ')
email_check(email)