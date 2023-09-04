# vamos a crear nuestras propias funciones, ver lo que podemos hacer y cómo las podemos usar

# tenemos que usar la palabra reservada def

'''
def <nombre de la funcion>():
    <sentencias>
'''

def saludo(nombre):
    print("Hola {}.".format(nombre))
    

nombre = input("Dime un nombre: ")
nombre=nombre.title()

saludo(nombre)

def tabla7():
    for i in range(11):
        print("7 x {} = {}".format(i, i*7))

tabla7()