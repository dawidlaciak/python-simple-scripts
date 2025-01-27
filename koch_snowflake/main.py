import turtle
 
def koch(length, level):
 
    if level == 0:
        turtle.forward(length)
        return
 
    new_length = length / 3.0
    koch(new_length, level - 1)
    turtle.left(60)
    koch(new_length, level - 1)
    turtle.right(120)
    koch(new_length, level -1)
    turtle.left(60)
    koch(new_length, level -1)
 
 
length = 500.0
 
turtle.speed(0)
turtle.penup()
turtle.goto(-length/2, length/4)
turtle.pendown()
 
for i in range(3):
    koch(length, 4)
    turtle.right(120)
 
turtle.hideturtle()
turtle.mainloop()