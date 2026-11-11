import turtle

sides = int(input("Enter the number of sides: "))
length = int(input("Enter the length of each side: "))

angle = 360 / sides

t = turtle.Turtle()
t.speed(5)

for petal in range(sides):
    for i in range(sides):
        t.forward(length)
        t.left(angle)
    t.left(angle)

turtle.done()