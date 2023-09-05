class FabricaTelefonos():
    pass #el pass es para no colocarle sentencias

print(type(FabricaTelefonos))

movil = FabricaTelefonos() #así creamos un objeto

print(type(movil)) #__main__ sería la clase raíz ; así podemos ver que este objeto está creado a partir de la clase FabricaTelefonos

fijo = FabricaTelefonos()

print(type(fijo))

def fabricaTelefonos():
    pass 


print(type(fabricaTelefonos())) # vemos como nos devuelve un conflicto, no sabe a cuál hacemos referencia, hay que tener cuidado con poner los mismos nombres aunque sean entidades destintas, por eso lo cambio a minúsucula
