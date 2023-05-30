# Abrir el archivo en modo lectura
with open('DIVIPOL_20220509_103027_01 (2) (1).txt', 'r', encoding='utf-8') as file:
    # Leer las líneas del archivo
    lines = file.readlines()

# Crear un diccionario vacío
datos =  {
    
    'departamento':{
    'ANTIOQUIA' : "01",
    'ATLANTICO' : "03",
    'BOLIVAR ' : "05",
    'BOYACA' : "07", 
    'CALDAS' : "09",
    'CAUCA' : "11",
    'CESAR' : "12",
    'CORDOBA' : "13",
    'CUNDINAMARCA' : "15",
    'BOGOTA D.C' : "16",
    'CHOCO ' : "17",
    'HUILA ' : "19",
    'MAGDALENA ' : "21",
    'NARI�O ' : "23",
    'RISARALDA ' : "24",
    'QUINDIO ' : "26",
    'SANTANDER ' : "27",
    'SUCRE ' : "28",
    'TOLIMA ' : "29",
    'VALLE ' : "31",
    'ARAUCA ' : "40",
    'CAQUETA ' : "44",
    'CASANARE ' : "46",
    'LA GUAJIRA ' : "48",
    'GUAINIA ' : "50",
    'META ' : "52",
    'GUAVIARE ' : "54",
    'SAN ANDRES ' : "56",
    'AMAZONAS ' : "60",
    'PUTUMAYO ' : "64",
    'VAUPES ' : "68",
    'VICHADA ' : "72",
    'CONSULADOS ' : "88",
    },

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
print(datos)
print("________________________________________________________________________________________________________________")



