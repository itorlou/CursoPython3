# una tupla es una lista que no se puede modificar
# son INMUTABLES

tupla = (1,2,3,4,5)

tupla2 = 6,7,8,9,10

print(tupla)

print (type(tupla))
print (type(tupla2))

# como buenas prácticas con las tuplas pondremos el paréntesis

# podemos acceder a un valor de la tupla

print(tupla[2])

print(tupla[ : 3]) #debanado de tuplas

print(tupla+tupla2) #sumamos
print(tupla,tupla2) #concatenamos

# tupla[2]=10 en las tuplas no se pueden modificar los valores