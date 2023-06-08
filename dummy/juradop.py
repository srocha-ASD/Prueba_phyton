import csv
import random
from datetime import datetime, timedelta


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
    idmesa = random.randint(1,50)

    # Generate a random unique name
    names = ['Adara Núñez ', 'Inna', 'Juan García ', 'Safia  JOHNSON', 'Santiago agudelo', 'Liam rubiano', 'Jesús diaz','Lara ovalle','Noah rolda','Jimena arrieta','Marta aristizabal'
            ,'Ben rubiano','Eleazar Martínez','Cesar agusto','Radu florinda','tony rogers','Mateo casallas','Víctor vega','Fabio duque','Zuzen uribe','Paken rojas']
    
    titular = random.choice(names)
    remanate = random.choice(names)
    adicional = random.choice(names)

    #fecha de nacimiento
    age_min = 18  # Minimum age
    age_max = 65  # Maximum age
    # Calculate the date of birth
    today = datetime.now()
    dob_max = today - timedelta(days=(age_min * 365))
    dob_min = today - timedelta(days=(age_max * 365))
    dob = random_date_of_birth(dob_min, dob_max)
    age = calculate_age(dob)

    #divipol
    divipol = random.choice(divipol_values)
    # Generate other random data
    gender = random.choice(['F', 'M'])
    return  gender, dob.strftime("%Y/%m/%d"),titular,remanate,adicional,divipol,idmesa


def random_date_of_birth(start_date, end_date):
    # Generate a random date of birth between start_date and end_date
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randint(0, days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date

def calculate_age(birth_date):
    # Calculate age based on the provided birth_date
    today = datetime.now()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age



# Number of rows to generate
num_rows = 100

# Generate data and write to CSV file
with open('Jurados.csv', 'w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    


    # Set to keep track of generated cc and names
    unique_data = set()

    for _ in range(num_rows):
        # Generate unique data
        data = generate_unique_data()

        # Check if the cc and name combination is already used
        while (data[2], data[3]) in unique_data:
            data = generate_unique_data()

        # Add the cc and name combination to the set
        unique_data.add((data[2], data[3]))

        # Write data to the CSV file
        writer.writerow(data)

print(f'{num_rows} rows of data have been generated and saved to data.csv.')
