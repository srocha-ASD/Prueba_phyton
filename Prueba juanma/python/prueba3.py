# Supongamos que tienes dos arrays con valores
array1 = [10, 20, 30, 40, 50]
array2 = [5, 15, 25, 35, 45]

# Crear un diccionario vacío para clasificar los valores
clasificacion = {}

# Iterar sobre los valores de los arrays y clasificarlos
for valor1, valor2 in zip(array1, array2):
    # Aplicar el criterio de clasificación basado en los valores
    if valor1 < 30:
        identificador = 'menor_30'
    else:
        identificador = 'mayor_30'

    # Verificar si el identificador ya existe en el diccionario
    if identificador not in clasificacion:
        clasificacion[identificador] = []

    # Agregar los valores al identificador correspondiente
    clasificacion[identificador].append((valor1, valor2))

# Imprimir los resultados de la clasificación
for identificador, valores in clasificacion.items():
    print(identificador)
    for valor1, valor2 in valores:
        print(valor1, valor2)
    print("--------------------")
