from turtle import Turtle

class States(Turtle):

    def __init__(self, x, y, name):
        super().__init__()
        self.x = x
        self.y = y
        self.name = name
        self.create_state()
        

    def create_state(self):
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(self.x, self.y)
        self.write(f"{self.name}", False, "center", ('Arial', 8, 'normal'))

