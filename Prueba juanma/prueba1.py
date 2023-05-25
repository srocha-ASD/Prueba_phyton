# Abrir el archivo en modo lectura
with open('DIVIPOL_20220509_103027_01 (2) (1).txt', 'r') as file:
    # Leer las líneas del archivo
    lines = file.readlines()

# Crear un diccionario vacío
diccionario = {}

# Recorrer cada línea del archivo
for line in lines:
    # Imprimir el diccionario resultante
    print(diccionario)
    # Obtener los campos de interés
    codigod = line[0:2].strip()
    codigom = line[2:5].strip()
    codigoz = line[5:7].strip()
    codigop = line[7:9].strip()
    nombred = line[19:31].strip()

    # Agregar los campos al diccionario
    diccionario['Codigo departamento'] = codigod
    diccionario['Codigo municipio'] = codigom
    diccionario['Codigo zona'] = codigoz
    diccionario['Codigo puesto'] = codigop
    diccionario['Nombre departamento'] = nombred


