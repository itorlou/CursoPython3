'''Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas'''

vocal = (input("introduce una vocal en minúscula: "))
letra = (input("Introduce una letra en mayúscula: "))

if vocal not in ('a','e','i','o','u'):
    print("No es una vocal minúscula")
elif letra.islower():
    print("No has introducido una letra mayúscula")
else:
    print(vocal.upper()+letra.lower())