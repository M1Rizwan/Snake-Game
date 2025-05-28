from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.marks = 0
        self.color("green")
        self.penup()
        self.goto(-20,   280)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.marks}", align="center", font=('arial', 12, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=('courier', 24, 'bold'))

    def increase_score(self):
        self.marks += 1
        self.clear()
        self.update_score()
