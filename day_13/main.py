# Historia: Eres un valiente explorador en busca de un tesoro escondido en una isla misteriosa.
# Para encontrar el tesoro, debes seguir una serie de instrucciones y llegar al destino final.
#
# Instrucciones:
#
# Partiendo desde tu posición inicial (0, 0), sigue las siguientes coordenadas: (2, 3), (-1, 5), (4, -2).
# Calcula la posición final sumando todas las coordenadas.
# Tu tarea es escribir un programa en Java que tome estas instrucciones y calcule la posición final del tesoro.


HOME = (0, 0)
x = 0
y = 0
COORDINATES = {
    'COORD': 3,
    'COORD_1': (2, 3),
    'COORD_2': (-1, 5),
    'COORD_3': (4, -2)
}
for n in range(1, COORDINATES['COORD']+1):
    x += COORDINATES[f'COORD_{str(n)}'][0]
    y += COORDINATES[f'COORD_{str(n)}'][1]
print(f'Coordenada final: ({HOME[0] + x}, {HOME[1] + y})')
