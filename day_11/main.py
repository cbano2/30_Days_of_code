#Un doctor en ENCRITACIÓN ha sido asesinado, su obsesión siempre fueron
#los MURCIELAGOS quienes tienen algo que ver en sus ultimas palabras
#su carta final fue una frase dirigida a una persona llamada
#TRISTEZA:
#"T24st5z7 S9y y9 d5 n15v9 H735 t450p9 q15 n9s v509s N9 p92q15 q14527 p529 b15n9 1st5d s450p25 05 q14s9 0as"
#-el codigo comienza desde el 0 hasta el 9

CLUE = 'MURCIELAGOS'
TEXT = 'T24st5z7 S9y y9 d5 n15v9 H735 t450p9 q15 n9s v509s N9 p92q15 q14527 p529 b15n9 1st5d s450p25 05 q14s9 0as'
clue_list = [l.lower() for l in CLUE]
text_list = [l for l in TEXT]
secret_text = ""
for l in text_list:
    if l.isdigit():
        secret_text += clue_list[int(l)]
    else:
        secret_text += l
print('El mensaje secreto es: ')
print(secret_text)