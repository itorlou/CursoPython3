diccionario = {'Nombre' : 'Isaac', 'Apellido1':'Torrado','Estatura':1.79}


print (diccionario)
# métodos para ver claves o valores

print(diccionario.keys()) #solo claves

print(diccionario.values()) #solo valores

print(diccionario['Estatura']) #llamamos el valor de una clave

# añadimos una clave/valor
diccionario['Peso'] = "87kg"

print(diccionario)

# modificamos el valor ya existente

diccionario['Nombre']= 'isaac'

print(diccionario)