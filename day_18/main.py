#Se le pide que se asegure de que el nombre y los apellidos de las personas empiecen por mayúscula en sus pasaportes.
#Por ejemplo, july herrera debe escribirse correctamente en mayúsculas como July Herrera.
#Dado un nombre completo, su tarea consiste en escribir el nombre en mayúsculas correctamente.

#Reglas:
#- La cadena está formada por caracteres alfanuméricos y espacios.

#Nota: en una palabra sólo se escribe en mayúsculas el primer carácter. Ejemplo 12abc cuando se escribe en mayúsculas sigue siendo 12abc.

#Input: chris alan
#Ouput: Chris Alan

#Input: 1 w 2 r 3g
#Output: 1 W 2 R 3g

def pascal_case(word: str) -> str:
    word = word.title()
    word_list = [l for l in word]
    for n in range(len(word)):
        if word_list[n].isdigit():
            if word_list[n+1].isupper():
                word_list[n+1] = word_list[n+1].lower()
    result = "".join(word_list)
    return result


word = input('Ingresa la palabra: ')
print(pascal_case(word))
