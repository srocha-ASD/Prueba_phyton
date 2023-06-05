import csv

# trae todos lo datos del txt
with open('DIVIPOL_20220509_103027_01 (2) (1).txt', 'r', encoding='utf-8') as file:
    # Leer las líneas del archivo
    lines = file.readlines()

    datos = []

    for line in lines:
        # Obtener campos de departamentos
        codigo_departamento = line[0:2].strip()
        nombre_departamento = line[9:21].strip()
        # Obtener campos de municipios
        codigo_municipio = line[2:5].strip()
        nombre_municipio = line[21:51].strip()
        # Obtener campos de puestos
        codigo_puesto = line[5:9].strip()
        nombre_puesto = line[51:91].strip()
        # Obtener indicador de puesto
        indicador_puesto = line[91:92].strip()
        # Obtener indicador de hombres
        hombres = line[92:100].strip()
        # Obtener indicador de mujeres
        mujeres = line[100:108].strip()
        # Obtener indicador de numero de mesas
        numero_mesas = line[108:114].strip()
        # Obtener codigo comuna
        codigo_comuna = line[114:116].strip()
        # Obtener nombre comuna
        nombre_comuna = line[116:146].strip()

        datos.append([codigo_departamento, nombre_departamento, codigo_municipio, nombre_municipio, codigo_puesto, nombre_puesto, indicador_puesto, hombres, mujeres, numero_mesas, codigo_comuna, nombre_comuna])

# Escribir los datos en un archivo CSV
with open('datos2.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(datos)
                