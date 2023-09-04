# como almacenar parámetros en tuplas y listas


def argumento(num):
    return type(num)
def argumento2(*num): #con el asterisco lo almacenamos en una tupla
    for i in num:
        print(i)

print(argumento(45))
print(argumento(45.01))
print(argumento("hola"))

print(argumento2("loren","ipsum","dollor","sit","amen"))