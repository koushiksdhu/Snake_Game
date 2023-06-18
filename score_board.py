from turtle import Turtle

# CONSTANTS
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")

class Scoreboard(Turtle):
    
    def __init__(self):         # Current class constructor.
        super().__init__()      # Calling the parent class constructor, i.e., Turtle class constructor.
        self.score = 0          # score variable for storing the score.
        self.high = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.color("#ffffff")   # Setting the color of the turtle.
        self.penup()            # Making penup.
        self.goto(0, 275)       # Goto a particular position.
        self.hideturtle()       # Hiding the turtle.
        self.score_write()      # Writing on the screen.
        
    def score_write(self):
        self.write(f"Score: {self.score}\tHigh Score: {self.high_score}", align = ALIGNMENT, font = FONT)   # Writing on the screen.
        
    def score_update(self):
        self.clear()        # Clearing the write method.
        self.score += 1     # Updating the score by 1.
        self.score_write()  # Writing the score on the screen.
        
    def game_over(self):
        self.goto(0, 0)     # Going to the middle position.
        if self.high_score < self.score:
            with open("high_score.txt", mode = "w") as file:
                    file.write(str(self.score))
        self.write("GAME IS OVER", align = ALIGNMENT, font = FONT)   # Writing on the screen.
        
        