import turtle

t = turtle.Turtle()
t.shapesize(2,2,3)
s = turtle.Screen()
s.bgcolor('white')

t.fillcolor('pink')
t.begin_fill()
t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)
t.end_fill()

