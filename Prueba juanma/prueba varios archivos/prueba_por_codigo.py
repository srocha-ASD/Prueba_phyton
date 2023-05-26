# Abrir el archivo en modo lectura
with open('DIVIPOL_20220509_103027_01 (2) (1).txt', 'r', encoding='utf-8') as file:
    # Leer las líneas del archivo
    lines = file.readlines()

# Crear un diccionario vacío
datos = {
    'departamento':{},
    'municipio':{},
    'puesto':{}
}


# Recorrer cada línea del archivo
for line in lines:
    # Obtener campos de departamnetos
    codigod = line[0:2].strip()
    nombred = line[9:21].strip()

    # Obtener campos de municipio
    codigom = line[2:5].strip()
    nombrem = line[21:51].strip()

    # Obtener campos de puestos
    codigop = line[5:9].strip()
    nombrep = line[51:91].strip()

    # Agregar los campos al diccionario
    datos['departamento'][codigod] = nombred
    datos['municipio'][codigom] = nombrem
    datos['puesto'][codigop] = nombrep

    




# Imprimir el diccionario resultante
print(datos)
print("________________________________________________________________________________________________________________")
print(len(datos))
print("________________________________________________________________________________________________________________")
print(datos['puesto']['9947'])
print("________________________________________________________________________________________________________________")



