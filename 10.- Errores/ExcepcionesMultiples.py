while True:
    try:
        num1 = int(input("Ingresa un numero: "))
        resultado = 100 / num1
        print(resultado)
        break
    except ValueError:
         print("Has colocado un valor erróneo.")
    except KeyboardInterrupt:
        print("\n Has cancelado la ejecución")
        break
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print("Tu edad es :",edad)
        break
    except KeyboardInterrupt:
        print("\n Has cancelado la ejecución.")
        break
    except ValueError:
         print("Has colocado un valor erróneo.")
