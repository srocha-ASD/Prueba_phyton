# Supongamos que tienes dos arrays con valores
# Abrir el archivo en modo lectura
with open('DIVIPOL_20220509_103027_01 (2) (1).txt', 'r') as file:
    # Leer las líneas del archivo
    lines = file.readlines()

for line in lines:
    array1 = line[0:2].strip()

# Crear un diccionario vacío para clasificar los valores

clasificacion = {}

# Iterar sobre los valores de los arrays y clasificarlos

for valor1 in array1:
    # Aplicar el criterio de clasificación basado en los valores

    if valor1 == 01:
        print(Medellin)
    else:
        print(prueba)

  