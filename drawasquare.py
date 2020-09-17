import turtle
def draw_square():
    window=turtle.Screen()
    window.bgcolor("red")
     
    brad=turtle.Turtle()
    brad.forward(200)
    brad.right(90)
    brad.forward(100)
    brad.left(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(200)
    brad.right(45)
    brad.forward(150)
    brad.right(45)
    brad.forward(100)
    
    window.exitonclick()
draw_square()
