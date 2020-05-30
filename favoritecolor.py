import turtle
t = turtle.Pen()
y = input("Enter your favorite color.")
for x in range(100):
    t.pencolor(y)
    t.circle(x)
    t.left(91)
