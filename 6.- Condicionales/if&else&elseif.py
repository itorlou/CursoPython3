# IF ELSE -----------------------

# queremos hacer un programa para determinar si el usuario es mayor de edad o no 

if int(input("Introduce tu edad: ")) >= 18:
    print("El usuario es MAYOR de Edad")
else:
    print("El usuario es MENOR de Edad")

# ELIF -----------------------

# Queremos hacer un programa que diga si la letra introducida es a, e, i, o, u

letra = (input("Introduce tu letra: "))

if letra.lower() not in ('a','e','i','o','u'):
    print("Esta letra es una vocal")
else:
    print("Esta letra no es una vocal")

if letra.lower()=='a':
    print("esta vocal es la A")
elif letra.lower()=='e':
    print("esta vocal es la E")
elif letra.lower()=='i':
    print("esta vocal es la I")
elif letra.lower()=='o':
    print("esta vocal es la O")
elif letra.lower()=='u':
    print("esta vocal es la U")
else:
    print("la letra introducida no es una vocal")

