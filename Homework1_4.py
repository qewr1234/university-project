import turtle

turtle.setup(500, 500)
t = turtle.Turtle()
t.shape("turtle")
t.pensize(4)
t.color("red")
t.pencolor("blue")

width, length = map(int, input("width and length = ").split())

t.dot(4)
t.write(t.pos())
t.up(); t.goto((-width/2, -length/2)); t.down()

t.forward(width); t.left(90)
t.forward(length); t.left(90)
t.forward(width); t.left(90)
t.forward(length); t.left(90)
t.up(); t.goto((0, 0)); t.down()

