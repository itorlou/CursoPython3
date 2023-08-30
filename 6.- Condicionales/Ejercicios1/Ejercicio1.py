'''Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal
'''

letra=input("Introduce una letra: ")

if letra.lower() not in ('a','e','i','o','u'):
    print ("La letra introducida no es una vocal")
else:
    print("La letra introducida es una vocal")