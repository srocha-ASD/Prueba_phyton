#importamos biblioteca
import yaml

#creamos el diccionario
datos = {}

# variables para editar
entrada = 'logstash\pipeline\python\DIVIPOL_20220509_103027_01 (2) (1).txt'
salida  = 'logstash/diccionario/diccionariodedatos.yml'

#leemos achivo
with open(entrada, 'r', encoding='utf-8') as file:
    # Leer las líneas del archivo
    lines = file.readlines()

# Recorrer cada línea del archivo
for line in lines:
    # Obtener divipolos
    divipol = line[0:9].strip()

    # Obtener campos de departamnetos
    codigod = line[0:2].strip()
    nombred = line[9:21].strip()

    # Obtener campos de municipio
    codigom = line[2:5].strip()
    nombrem = line[21:51].strip()

    # Obtener campos de puestos
    nombrez = line[5:7].strip()

    # Obtener campos de puestos
    codigop = line[7:9].strip()
    nombrep = line[51:91].strip()

    # Obtener campos de puestos
    numerom = line[108:114].strip()

    #creamos un diccionario con la lista line por linea
    datos_d = {codigod : nombred}
    datos_m = {codigom : nombrem}
    datos_z = {nombrez : nombrez}
    datos_p = {codigop : nombrep}
    datos_me = {numerom : numerom}

    # creamos el diccionario
    datos[divipol] = []

    # Agregar el diccionario a la lista de datos
    datos[divipol].append(datos_d)
    datos[divipol].append(datos_m)
    datos[divipol].append(datos_z)
    datos[divipol].append(datos_p)
    datos[divipol].append(datos_me)

    

# guardamos todo en un archivho yaml 
with open(salida, 'w', encoding='utf-8') as f:
    yaml.dump(datos, f, default_flow_style=False, allow_unicode=True, default_style="'") 
    #el default_flow_style=False es para que me organice los datos