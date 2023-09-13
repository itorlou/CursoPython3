import turtle
import random # para importar el dado

s = turtle.Screen()
s.title("Carrera tortugas")
#creamos los jugadores
jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()
#cambiamos el fondo
s.bgcolor("gray")
#le damos forma al jugador 1
jugador1.hideturtle()
jugador1.shape("turtle")
jugador1.color("green")
jugador1.shapesize(2,2,2)
jugador1.pensize(3)
#le damos forma al jugador 1
jugador2.hideturtle()
jugador2.shape("turtle")
jugador2.color("blue")
jugador2.shapesize(2,2,2)
jugador2.pensize(3)

#dibujamos las metas
jugador1.penup()
jugador1.goto(200,200)
jugador1.pendown()
jugador1.circle(40)

jugador2.penup()
jugador2.goto(200,-200)
jugador2.pendown()
jugador2.circle(40)

#dibujamos las tortugas
jugador1.penup()
jugador1.goto(-250,225)
jugador1.showturtle()


jugador2.penup()
jugador2.goto(-250,-170)
jugador2.showturtle()

dado = [1,2,3,4,5,6]  # iniciamos un array para los resultados del dado

for i in range(20):
    #si terminan las tortugas finalizamos
    if jugador1.pos() >= (200,200):
        print("La tortuga verde ha ganado")
        break

    elif jugador2.pos() >= (200,-200):
        print("La tortuga azul ha ganado")
        break
    #sino pasamos al turno 
    else:
        turno1 = input("Presiona Enter para continuar")
        turno1 = random.choice(dado)
        print("Tu numero en dado es: ",turno1," Avanzas: ",turno1*20)
        jugador1.pendown()
        jugador1.forward(20*turno1)

        turno2 = input("Presiona Enter para continuar")
        turno2 = random.choice(dado)
        print("Tu numero en dado es: ",turno2," Avanzas: ",turno2*20)
        jugador2.pendown()
        jugador2.forward(20*turno2)

turtle.done()