import json
#trae los datos organizados y relacionados pero no los divide por columnas separas en el json
# Abrir el archivo de texto
with open('DIVIPOL_20220509_103027_01 (2) (1).txt', 'r', encoding='utf-8') as file:
    # Leer las líneas del archivo
    lines = file.readlines()

    datos = []

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

        # Agregar los campos como pares de codigod y nombred
        registro = {
            'codigod': codigod,
            'nombred': nombred,
            'codigom': codigom,
            'nombrem': nombrem,
            'codigop': codigop,
            'nombrep': nombrep
        }

        datos.append(registro)

# Escribir los datos en un archivo JSON
with open('datos_json.json', 'w') as file:
    json.dump(datos, file)