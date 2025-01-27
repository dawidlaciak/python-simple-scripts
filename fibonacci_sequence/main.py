import turtle

def fibonacci(n:int) -> list:
    
    fibonacci_sequence = []
    value1 = 0
    value2 = 1

    for i in range(n):

        fibonacci_sequence.append(value2)
        value1, value2 = value2, value1 + value2
    
    return fibonacci_sequence


def square(length, increase):

    for i in range(4):
        turtle.forward(length * increase)
        turtle.right(90)


def generate_fibonacci_squares(fibonacci_sequence:list, width:int, height:int, increase:int):

    screen = turtle.Screen()
    screen.setup(width + 10, height + 10)
    
    turtle.penup()
    turtle.goto(-width / 4, height / 4)
    turtle.pendown()

    for value in fibonacci_sequence:
        square(value, increase)
        turtle.penup()
        turtle.forward(value * increase)
        turtle.right(90)
        turtle.forward(value * increase)
        turtle.pendown()

    turtle.mainloop()

fibonacci_sequence = fibonacci(10)
generate_fibonacci_squares(fibonacci_sequence, 400, 600, 5)
