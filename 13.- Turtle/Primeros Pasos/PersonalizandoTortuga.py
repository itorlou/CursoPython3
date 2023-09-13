import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("pink") #color del fondo
s.title("Proyecto 1") #título de la ventana

#modificamos el tamaño de la tortuga
t.shapesize(1,5,10)
t.shapesize(10,5,1)
t.shapesize(1,10,5)
t.shapesize(10,1,5)

t.pensize(20) # cambiamos el tamaño del trazo
t.forward(100)

t.shapesize(3,3,3)
t.fillcolor("orange") #cambiar el color de la tortuga
t.pencolor("white") #cambiamos el color del lápiz
t.goto(200,-200)

t.color("green", "black") #cambiamos el color de la tortuga y de la tinta
t.forward(50)

turtle.done()