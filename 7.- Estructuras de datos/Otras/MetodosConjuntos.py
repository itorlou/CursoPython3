conjunto = {1,2,3,4,5}
lista = [1,1,2,3,4,4]

print(lista)
print(conjunto) #notamos que no imprime los datos repetidos

conjunto.add(20) #añadimos un valor

print(conjunto)

conjunto.remove(1) #elimina el valor que especifiquemos

print(conjunto)

# conjunto.pop() #toma cualquier valor al azar y lo elimina

print(conjunto)

conjunto.update([1,2,3]) #añade un elemento iterable

print(conjunto)

conjunto.clear() #deja el conjunto vacío

print (conjunto)