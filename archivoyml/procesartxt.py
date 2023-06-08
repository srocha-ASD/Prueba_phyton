#importamos biblioteca
import yaml

#creamos el diccionario
datos = {}

# creamos el diccionario
datos['departamento'] = []
datos['municipio'] = []
datos['zona'] = []
datos['puesto'] = []
datos['numeromesas'] = []

# variables para editar
entrada = 'Prueba_phyton\DIVIPOL_20220509_103027_01 (2) (1).txt'
salida  = 'Prueba_phyton\aarchivoyml'

#leemos achivo
with open(entrada, 'r', encoding='utf-8') as file:
    # Leer las líneas del archivo
    lines = file.readlines()
# Recorrer cada línea del archivo
for line in lines:
    # Obtener divipolos
    divipol = line[0:9].strip()
    # Obtener campos de departamnetos
    nombred = line[9:21].strip()
    # Obtener campos de municipio
    nombrem = line[21:51].strip()
    # Obtener campos de puestos
    nombrez = line[5:7].strip()
    # Obtener campos de puestos
    nombrep = line[51:91].strip()
    # Obtener campos de puestos
    numerom = line[108:114].strip()

    #creamos un diccionario con la lista line por linea
    datos_d = {divipol : nombred}
    datos_m = {divipol : nombrem}
    datos_z = {divipol : nombrez}
    datos_p = {divipol : nombrep}
    datos_me = {divipol : numerom}
    # Agregar el diccionario a la lista de datos
    datos['departamento'].append(datos_d)
    datos['municipio'].append(datos_m)
    datos['zona'].append(datos_z)
    datos['puesto'].append(datos_p)
    datos['numeromesas'].append(datos_me)

    

# guardamos todo en un archivho yaml 
with open(salida, 'w', encoding='utf-8') as f:
    yaml.dump(datos, f, default_flow_style=False, allow_unicode=True, default_style="'") 
    #el default_flow_style=False es para que me organice los datos