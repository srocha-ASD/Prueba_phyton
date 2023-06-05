num1=int(input("Ingrese la cantidad de preguntas: "))
num2=int(input("Ingrese cantidfad de correctas: "))
prometidio= (num2 * 100)/num1

if prometidio < 50:
    print("Perdio")

elif prometidio >= 50 & prometidio < 75:

    print("Regular")

elif prometidio >=75 & prometidio < 90:

    print("Medio")
else:
    
    print("Maximo")
