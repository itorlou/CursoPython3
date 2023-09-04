# vamos a ver el retorno de valores, en algunas funciones podemos establecer el valor a regresar
'''
def <nombreFuncion>():
    <sentencias>
    return <valor a retornar>'''

def entero():
    print('Este es un dato entero: ')
    return 10

print (entero()) #tenemos que ponerlo entre paréntesis

def decimal():
    print('Este es un dato decimal: ')
    return 90.99

print(decimal())

def frase():
    return "Esto es una frase"

print(frase())

# hay otro tipo de funciones que devuelven un valor, que es la asignación

def asignacion():
    return 1,2,3,4,5

lista = (asignacion())

print(lista)

a,b,c,d,e=asignacion()

print(a,b,c,d,e)