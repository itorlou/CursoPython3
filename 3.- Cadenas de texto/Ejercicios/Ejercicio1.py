'''Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:'''

cadena = "Te quiero solo como amigo"

# Imprima los dos primeros caracteres.

print (cadena[0:2])

# • Imprima los tres últimos caracteres.

print (cadena[-3: ])

# • Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

print(cadena[ : : 2]) # : "recorre todo" | : 2 cada 2 caracteres

# • Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

print(cadena[: : -1]) # : "recorre todo" | : -1 imprime todo pero a la inversa

# • Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.'''

print(cadena+cadena[: : -1])