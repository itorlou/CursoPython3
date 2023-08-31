diccionario = {'Usuario':'itorlou','Password':12345}

print(diccionario)
print(type(diccionario)) 

# si añadimos otra clave-valor con la misma clave la va a sobreescribir
diccionario = {'Usuario':'itorlou','Password':12345,'Usuario':'yaito'}
print(diccionario)