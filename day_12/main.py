#Mission Impossible: Beat the panther_Reto 12

  #Escribe una función que reciba dos palabras (String) y retorne
 # verdadero o falso (Bool) según sean o no anagramas.
 #- Un Anagrama consiste en formar una palabra reordenando TODAS
 #  las letras de otra palabra inicial.
 # - NO hace falta comprobar que ambas palabras existan.
 # - Dos palabras exactamente iguales no son anagrama.


def check_words(word_1: str, word_2: str) -> bool:
    word_check = [letter for letter in word_1 if letter in word_2]
    if len(word_check) == len(word_2):
        return True
    else:
        return False


word_1 = input('Ingrese la primera palabra: ')
word_2 = input('Ingrese la segunda palabra: ')

if check_words(word_1, word_2):
    print(f'La palabra ({word_1}) y la palabra ({word_2}) son anagramas')
else:
    print('Estas palabras no son un anagrama')
