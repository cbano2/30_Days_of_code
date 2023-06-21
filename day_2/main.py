from unit_convert import UnitConvert

print('CONVERSOR DE UNIDADES DE MEDIDA')

unit_list = UnitConvert(meters=1).keys()
unit = [u for u in unit_list if len(u) < 3]
description = [d for d in unit_list if len(d) > 3]
unit_dict = {
    'unit': unit,
    'description': description
}

print("Detalles de conversión: ")
for n in range(len(unit_dict['unit'])):
    print(f"Unidad: {unit_dict['unit'][n]}, Descripción: {unit_dict['description'][n]}")
data = input('Ingrese en el siguiente formato: número,unidad,unidad_destino(sin espacios):\n')
data_list = data.split(',')
value = float(data_list[0])
from_unit = data_list[1].lower()
to_unit = data_list[2].lower()
print(f"La unidad convertida es: {UnitConvert(from_unit, value)[to_unit]}")





