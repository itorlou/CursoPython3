import turtle

s = turtle.Screen()
t = turtle.Turtle()

'''t.begin_fill() #empieza a definir las figuras a rellenar
t.circle(100)
t.end_fill() #delimita el final de las figuras a rellenar 

t.begin_fill()
t.color("white", "white")
t.circle(50)
t.end_fill()'''

t.shape("turtle") #cambiamos la forma del lapiz:square,arrow, circle, triangle, classic, turtle 

t.forward(100)
t.penup() #levanta la figura y no dibuja nada
t.forward(50)
t.pendown() #vuelve a bajar el lápiz
t.forward(100)

t.undo() #como un retroceso
t.clear() #limpia toda la pantalla
t.reset() #se reinicia el programa por completo

t.forward(100)
t.stamp() # deja un sello (con la marca del lápiz)
t.forward(100)

turtle.done()