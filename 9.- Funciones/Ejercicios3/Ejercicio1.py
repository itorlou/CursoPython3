# Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio


def areaCuadrado(base,altura):
    return base*altura

def areaCirculo(radio):
    import math
    return math.pi * pow(radio,2)

print(areaCuadrado(2,2))

print(areaCirculo(10))
    