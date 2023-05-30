import json
#trae los datos por columnas pero no los organiza 
# Abrir el archivo de texto
with open('DIVIPOL_20220509_103027_01 (2) (1).txt', 'r', encoding='utf-8') as file:
    # Leer las líneas del archivo
    lines = file.readlines()

    datos = {
        'codigod': [],
        'nombred': [],
        'codigom': [],
        'nombrem': [],
        'codigop': [],
        'nombrep': []
    }

    for line in lines:
        # Obtener campos de departamentos
        codigod = line[0:2].strip()
        nombred = line[9:21].strip()

        # Obtener campos de municipios
        codigom = line[2:5].strip()
        nombrem = line[21:51].strip()

        # Obtener campos de puestos
        codigop = line[5:9].strip()
        nombrep = line[51:91].strip()

        # Agregar los campos a las columnas correspondientes
        datos['codigod'].append(codigod)
        datos['nombred'].append(nombred)
        datos['codigom'].append(codigom)
        datos['nombrem'].append(nombrem)
        datos['codigop'].append(codigop)
        datos['nombrep'].append(nombrep)

# Escribir los datos en un archivo JSON
with open('datos_json.json', 'w') as file:
    json.dump(datos, file)