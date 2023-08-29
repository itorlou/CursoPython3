#nombre documentación = substrings

# al fin y al cabo una string es una concatenación de caracteres

cadena = "Este es un ejemplo de Substring (Debanado de Cadenas)"

print(len(cadena)) #longitud de la cadena

#Substring toma el espacio que ocupa cada caracter

print(cadena[2])
print(cadena[50])
print(cadena[0])
print(cadena[7])

print(cadena[0:9])
print(cadena[ :20]) # 20 primeros caracteres
print(cadena[20 : ]) # 20 finales caracteres
print(cadena[-1]) # con valores negativos cuenta desde atrás