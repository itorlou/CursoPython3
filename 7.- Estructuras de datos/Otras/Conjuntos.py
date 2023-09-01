# la sintaxis de conjuntos puede ser () [] {}

conjunto = {1,2,3,4,5} #ponemos las llaves de diccionario pero los valores como si fuese una lista 

conjunto2 = set[(1,2,3,4,5)] # type: ignore

conjunto3 = set((1,2,3,4,5))

print (type(conjunto))

print (type(conjunto2))

print (type(conjunto3))