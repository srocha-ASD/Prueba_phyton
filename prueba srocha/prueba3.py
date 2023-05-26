with open('DIVIPOL_20220509_103027_01 (2) (1).txt', 'r') as file:
 lines = file.readlines()

# Crear un diccionario vacío

departamentos = {}

# Recorrer cada línea del archivo

for line in lines:
 codigod = line[0:2].strip()
 nombred = line[9:21].strip()

# Agregar los campos al diccionario

 departamentos[f"{nombred}"] = codigod


print(departamentos)