import csv

# Abrir el archivo de texto
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

        datos.append([divipol, nombre_departamento, nombre_municipio, nombre_puesto,indicador_puesto,numero_mesas])

# Escribir los datos en un archivo CSV
with open('datos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(datos)