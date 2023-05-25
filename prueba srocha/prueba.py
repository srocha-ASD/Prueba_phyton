with open ('DIVIPOL_20220509_103027_01 (2) (1).txt', 'r') as file:
    lines = file.readlines()


diccionario = {}

for line in lines:

    codigod = line[0:2].strip()
    codigom = line[2:5].strip()
    codigoz = line[5:7].strip()
    codigop = line[7:9].strip()
    nombred = line[9:21].strip()
    nombrem = line[21:51].strip()
    nombrep = line[51:91].strip()
    indicadorp = line[91:92].strip()
    potenciah = line[92:100].strip()
    potenciam = line[100:108].strip()
    numerom = line[108:114].strip()
    

    print(diccionario)

    diccionario['Codigo de departamento'] = codigod
    diccionario['Codigo municipio'] = codigom
    diccionario['Codigo zona'] = codigoz
    diccionario['Codigo puesto'] = codigop
    diccionario['Nombre departamento'] = nombred
    diccionario['Nombre municipio'] = nombrem
    diccionario['Nombre puesto'] = nombrep
    diccionario['Indicador puesto'] = indicadorp
    diccionario['Potencial hombres'] = potenciah
    diccionario['Potencial mujeres'] = potenciam
    diccionario['Numero mesa'] = numerom


