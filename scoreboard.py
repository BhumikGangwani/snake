from turtle import Turtle

# Values that can be changed with preference
ALIGNMENT = "center"
FONT = ("Courier", 25, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # gets the all time highscore from the txt file
        with open("highscore.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.ht()
        self.pu()
        self.color("white")
        self.goto(0, 265)
        self.display_score()

    # Displays the current score and the highscore
    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", font=FONT, align=ALIGNMENT)

    # Resizes the snake and resets the game to the start position
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.display_score()

    def update_score(self):
        self.score += 1
