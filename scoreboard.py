from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__() #inherited everything from Turtle class
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        self.hideturtle()
    
    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)