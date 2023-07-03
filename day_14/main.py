#Mission Impossible: Beat the panther_Reto 14

#Dificultad media
#La carrera de tortugas

#Historia: En una carrera de tortugas, cada tortuga tiene un número asignado
# que indica su velocidad. Queremos determinar qué tortuga ganó la carrera.

#Instrucciones:

#1. Escribe un programa en Java que tome como entrada los números de velocidad de tres tortugas.
#2. El programa debe comparar los números de velocidad y determinar cuál es el más grande.
#3. Imprime el número de la tortuga ganadora.

speeds = [
    float(input("Velocidad Tortuga 1: ")),
    float(input("Velocidad Tortuga 2: ")),
    float(input("Velocidad Tortuga 3: "))
]
print(f"La tortuga ganadora es la que tiene la velocidad de {max(speeds)}")
