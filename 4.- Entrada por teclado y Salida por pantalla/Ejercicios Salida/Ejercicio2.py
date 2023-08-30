'''Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>

'''

Nombre =input("Introduce tu nombre: ")
Edad = int(input("Introduce tu edad: "))
Sexo = input("Introduce tu sexo: ")

print("Te llamas {} \n\nTu edad es: {}\n\nEres: {}".format(Nombre.capitalize(),Edad,Sexo.capitalize()))