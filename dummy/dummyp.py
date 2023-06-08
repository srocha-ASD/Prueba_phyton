import csv
import random

divipol_values=[]

with open('DIVIPOL_20220509_103027_01 (2) (1).txt', 'r', encoding='utf-8') as file:
    # Leer las líneas del archivo
    lines = file.readlines()

    for line in lines:

        divipol2 = line[0:9].strip()
        divipol_values.append(divipol2)
        

def generate_unique_data():
    # Generate a random unique cc (identification number)
    #divipol = random.choice(divipol2)
    cc = random.randint(1000000000, 9999999999)

    # Generate a random unique name
    names =  ['Adara Núñez ', 'Inna', 'Juan García ', 'Safia  JOHNSON', 'Santiago agudelo', 'Liam rubiano', 'Jesús diaz','Lara ovalle','Noah rolda','Jimena arrieta','Marta aristizabal'
            ,'Ben rubiano','Eleazar Martínez','Cesar agusto','Radu florinda','tony rogers','Mateo casallas','Víctor vega','Fabio duque','Zuzen uribe','Paken rojas']
    name = random.choice(names)

    #divipol

    divipol = random.choice(divipol_values)
    # Generate other random data
    gender = random.choice(['F', 'M'])
    age = random.randint(18, 65)
    novedad = random.choice(
        ['Sufragante no encontrado en ANI', 'nombres y/o apellidos ilegibles','nombre y/o apellido no concuerda con ANI'])

    return  divipol,cc, name, gender, age, novedad

#datos.append([divipol, cc, name, gender, age, novedad])


# Number of rows to generate
num_rows = 13261

# Generate data and write to CSV file
with open('Dummy.csv', 'w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    


    # Set to keep track of generated cc and names
    unique_data = set()

    for _ in range(num_rows):
        # Generate unique data
        data = generate_unique_data()

        # Check if the cc and name combination is already used
        while (data[0], data[1]) in unique_data:
            data = generate_unique_data()

        # Add the cc and name combination to the set
        unique_data.add((data[0], data[1]))

        # Write data to the CSV file
        writer.writerow(data)

print(f'{num_rows} rows of data have been generated and saved to data.csv.')
