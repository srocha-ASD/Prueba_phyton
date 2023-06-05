num1 =int(input("Ingresa el sueldo: "))
num2 =int(input("INgresa los años de antiguedad: "))

iva1 = num1 * 0.20
iva2 = num1 * 0.5

if (num1 < 500) & (num2 >= 10):

    print("Su sueldo final es: ",iva1)

elif (num1 < 500) & (num2 < 10):

    print("Su sueldo final es : ",iva2)

elif (num1 >= 500) & (num2 < 10):

    print("Su sueldo no tiene modificaciones: ", num1)
else:
    print("f")
