diccionario = {1:2,2:3,3:4}
diccionario2={4:5,6:7}

print(diccionario)

diccionario.pop(3) #borra la clave/valor que especifiquemos

print(diccionario)

# diccionario.clear() #limpiamos el diccionario


print(diccionario.get(2)) 

diccionario.setdefault(4,5) #añadimos un valor

print(diccionario)

diccionario.update(diccionario2) #añade los valores del 2 en el dicionario original, si hay una llave repetida se va a mantener sólo una

print(diccionario)

diccionario.copy()
print(diccionario)

