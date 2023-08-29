'''Ejercicio 2

Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r

Pista: Debes utilizar un método de las cadenas llamado “Replace”, recuerda que la posición de los caracteres empieza en 0.'''


cadena='Separado'
print (cadena)
# test de replace
print (cadena.replace("a", "e"))
# solución del ejercicio

print (cadena[0]+
    cadena[1:-1].replace("",',')+
    cadena[int(len(cadena))-1])