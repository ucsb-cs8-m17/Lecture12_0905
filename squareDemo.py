import turtle

if __name__=="__main__":
    t = turtle.Turtle()
    t.color("green")
    t.shape("turtle")


def drawSquare(side):
    t = turtle.Turtle()
    t.color('red')
    for i in range(4):
        t.forward(side)
        t.left(90)
