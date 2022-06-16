operacion = input("Que operación desea realizar? \n-Suma\n-Resta\n-Producto\n-Cociente\n-Modulo\n-Radicación\n-Potencia\n"  )

# ---------------------------------------------SUMA-----------------------------------------------------

if operacion == "Suma":

    num1 = int(input("Primer parámetro: "))

    num2 = int(input("Segundo parámetro: "))

    suma = num1 + num2

    print("El resultado es {}".format(suma)) 

 # ---------------------------------------------RESTA-----------------------------------------------------  

elif operacion == "Resta":

    num1 = int(input("Primer parámetro: "))

    num2 = int(input("Segundo parámetro: "))

    resta = num1 - num2

    print("El resultado es {}".format(resta))

# ---------------------------------------------PRODUCTO-----------------------------------------------------

elif operacion == "Producto":

    num1 = int(input("Primer parámetro: "))

    num2 = int(input("Segundo parámetro: "))

    producto = num1 * num2

    print("El resultado es {}".format(producto))

# ---------------------------------------------COCIENTE-----------------------------------------------------

elif operacion == "Cociente":

    num1 = int(input("Primer parámetro: "))

    num2 = int(input("Segundo parámetro: "))

    cociente = num1 / num2

    print("El resultado es {}".format(cociente))

# ---------------------------------------------MODULO-----------------------------------------------------

elif operacion == "Modulo":

    num1 = int(input("Primer parámetro: "))

    num2 = int(input("Segundo parámetro: "))

    modulo = num1 % num2

    print("El resultado es {}".format(modulo))

# ---------------------------------------------RADICACION-----------------------------------------------------

elif operacion == "Radicacion":

    num1 = int(input("Primer parámetro: "))

    num2 = int(input("Segundo parámetro: "))

    num2_radicando = 1 / num2
    radicacion =pow(num1, num2_radicando)

    print("El resultado es {}".format(radicacion))

# ---------------------------------------------POTENCIA-----------------------------------------------------

elif operacion == "Potencia":

    num1 = int(input("Primer parámetro: "))

    num2 = int(input("Segundo parámetro: "))

    potencia = pow(num1, num2)

    print("El resultado es {}".format(potencia))

else:
    print("Comando no válido, asegurate de usar mayuscula al inicio y sin tilde.")