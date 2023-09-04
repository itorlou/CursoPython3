# Escribir una función que reciba un número entero positivo y devuelva su factorial.



numero = int(input("Dime un número:"))

def factorial(numero):
    from math import factorial
    if numero < 0:
        print("El numero es negativo, no podemos proceder")
    else:
        print("El factorial es {}".format(factorial(numero)))

factorial(numero)

