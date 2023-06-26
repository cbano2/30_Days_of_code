# Fácil: Contar palabras en una cadena
# Desafío: Escribe una función que tome una cadena de texto y cuente cuántas
# palabras hay en ella. Puedes asumir que las palabras están separadas por
#  espacios y que no hay puntuación adicional.

def count_word(text: str):
    word_list = text.split(' ')
    words = len(word_list)
    print(f"El número de palabras es: {words}")


text = input('Introduce tu texto: ')
count_word(text)
