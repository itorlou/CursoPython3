#hay palabras reservadas que no se pueden usar

# print = 120

# print (print)

#como ver las palabras reservadas

# usaremos la librería keyword
import keyword 

print(keyword.kwlist)

# las variables serían:
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# las variables no pueden empezar por números
# las variables no pueden llevar carácteres especiales (a excepción de _)
# las variables no pueden llevar espacios