import json

# Filtra los datos del txt 
with open('DIVIPOL_20220509_103027_01 (2) (1).txt', 'r', encoding='utf-8') as file:
    # Leer las líneas del archivo
    lines = file.readlines()

    datos = []

    for line in lines:

        # Obtener campos de divipol
        divipol = line[0:9].strip()
        # Obtener campos de departamentos
        nombre_departamento = line[9:21].strip()
        # Obtener campos de municipios
        nombre_municipio = line[21:51].strip()
        # Obtener campos de puestos
        nombre_puesto = line[51:91].strip()
        # Obtener indicador de puesto
        indicador_puesto = line[91:92].strip()
        # Obtener indicador de hombres
        #hombres = line[92:100].strip()
        # Obtener indicador de mujeres
        #mujeres = line[100:108].strip()
        # Obtener indicador de numero de mesas
        numero_mesas = line[108:114].strip()
        # Obtener codigo comuna
        #codigo_comuna = line[114:116].strip()
        # Obtener nombre comuna
        #nombre_comuna = line[116:146].strip()

        # Agregar los campos como una fila en la lista de datos

        fila = {

            'divipol': divipol,
            #'codigo_departamento': codigo_departamento,
            'nombre_departamento': nombre_departamento,
            #'codigo_municipio': codigo_municipio,
            'nombre_municipio': nombre_municipio,
            #'codigo_puesto': codigo_puesto,
            'nombre_puesto': nombre_puesto,
            'indicador_puesto': indicador_puesto,
            #'hombres': hombres,
            #'mujeres':  mujeres,
            'numero_mesas': numero_mesas,
            #'codigo_comuna': codigo_comuna,
            #'nombre_comuna': nombre_comuna
        }

        datos.append(fila)

 # Escribir los datos en un archivo JSON
with open('datos_J.json', 'w', encoding='utf-8') as file:
    json.dump(datos, file,ensure_ascii=False ,indent=4)
