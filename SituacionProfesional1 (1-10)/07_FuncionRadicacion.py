#Función Radicación

a=int(input("Ingese el primer número: "))
b=int(input("Ingrese la raiz: "))

def radicacion(a, b):
    c=a**(1/b)
    print("El resultado de la raiz", b, " de ", a , " es: ", c)

radicacion(a, b)
