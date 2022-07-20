# Funcion Potencia

a=int(input("Ingese el primer número: "))
b=int(input("Ingrese el exponente: "))

def potencia(a, b):
    c=a**b
    print("El resultado de ", a, " exponente ", b , " es: ", c)

potencia(a, b)
