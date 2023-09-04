# hay que ponerse en la situación de que el usuario ingresa un str en vez de un entero

while True: #ponemos el while para que siga repitiendo en bucle 
    try:
        edad = int(input("Ingrese tu edad: "))
        print("Tu edad es:",edad)
        break #así finalizamos el bucle cuando el usuario introduzca un número
    except:
        print("Ingresaste un valor erróneo")
    finally:
        print("=============")
    