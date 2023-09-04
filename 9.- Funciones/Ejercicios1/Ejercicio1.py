# Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas

lista =[]

def crealista():
    i= 0
    while i <= 5:
        nuevoValor = float(input("Dime un numero: "))
        lista.append(nuevoValor)
        i +=1
    


def separarPares(lista):
    lista.sort()
    listapares=[]
    listaimpares=[]
    for i in lista:
        if i%2==0:
            listapares.append(i)
        else:
            listaimpares.append(i)
    print ("Los valores pares son ",listapares)
    print ("Los valores impares son ",listaimpares)

crealista()

separarPares(lista)