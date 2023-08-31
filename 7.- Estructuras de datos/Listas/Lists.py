# po

# pueden ser homogéneas (mismo tipo de datos) o heterogéneas (varios tipos de datos)

lista = ['Python',120,'Nombre',4.14, 6.28]

print(type(lista)) # vemos que es de class list

# vamos a llamar uno de estos datos según la posición
print(lista)
print(lista[3])

print(len(lista)) #podemos ver el número de elementos de la lista

# las listas son mutables, podemos cambiar su valor

lista[0]=lista[0].lower()

print(lista[0])