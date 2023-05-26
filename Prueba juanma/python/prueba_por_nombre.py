# Abrir el archivo en modo lectura
with open('DIVIPOL_20220509_103027_01 (2) (1).txt', 'r', encoding='utf-8') as file:
    # Leer las líneas del archivo
    lines = file.readlines()

# Crear un diccionario vacío
departamentos = {}
municipios = {}
puesto = {}

# Recorrer cada línea del archivo
for line in lines:
    # Obtener campos de departamnetos
    codigod = line[0:2].strip()
    nombred = line[9:21].strip()

    # Obtener campos de municipio
    codigom = line[2:5].strip()
    nombrem = line[21:51].strip()

    # Obtener campos de puestos
    codigop = line[7:9].strip()
    nombrep = line[51:91].strip()


    # Agregar los campos al diccionario
    municipios[nombred] = codigod
    municipios[nombrem] = codigom
    puesto[nombrep] = codigop


# Imprimir el diccionario resultante
"""print(departamentos)
print("________________________________________________________________________________________________________________")"""
print(municipios)
print("________________________________________________________________________________________________________________")
print(len(municipios))
print("________________________________________________________________________________________________________________")
print(municipios['CONSULADOS'])
"""print(puesto)
print("________________________________________________________________________________________________________________")
print(departamentos['ANTIOQUIA']+municipios['MEDELLIN']+puesto['SEC. ESC. LA ESPERANZA NO 2'])"""