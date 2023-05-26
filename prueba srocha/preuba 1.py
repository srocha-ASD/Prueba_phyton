

with open ('DIVIPOL_20220509_103027_01 (2) (1).txt', 'r') as file:
    lines = file.readlines()


diccionario = {}

for line in lines:

    codigod = line[0:2].strip()


    print(diccionario)

    diccionario['Codigo de departamento'] = codigod
    


 if codigod  == '01':

   print'(Medellin')

 else:

   print('prueba')