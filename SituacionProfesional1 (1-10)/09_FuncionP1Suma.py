# Función P1 Suma

a=float(input("Ingese el primer número a: "))
b=float(input("Ingrese el segundo número b: "))
c=float(input("Ingrese el tercer número c: "))

def p1(a, b, c):
    d=(a+b)*c
    print("Los números ingresados son: a=", a, " b=", b, " c=", c)
    print("El resultado de (a+b)*c es: ", d)

p1(a, b, c)
