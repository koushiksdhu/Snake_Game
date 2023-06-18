from turtle import Turtle, Screen
# In Python, Constants are written in CAPS.

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]    # STARTING_POSITION is a constant tuple (containing x and y coordinates), inside a list named, starting_position.
MOVE_DISTANCE = 20  # Constant moving distance.
MOVE_LEFT = 180     
MOVE_RIGHT = 0
MOVE_UP = 90
MOVE_DOWN = 270

class Snake:            # In python class name is always in pascal case.
    
    def __init__(self):     # Default constructor for class Snake.
        self.segments = []  # List segments.
        self.create_snake() # calling function create_snake.
        self.head = self.segments[0]    # Storing the first element of the list or head of the snake in the variable head.
        
    def create_snake(self): # function create_snake.
        for pos in STARTING_POSITIONS:  # Creating the body of the snake using loop.
            self.add_segment(pos)       # Calling the add_segment method.
            
    def add_segment(self, position):    # This is add_segment method.
        new_segment = Turtle(shape="square")    # Creating turtle of square shape.
        new_segment.color("white", "white")     # Setting up the color of the turtle.
        new_segment.penup()                     # penup commmand.
        new_segment.goto(position)              # Setting up the position of the turtle.
        self.segments.append(new_segment)       # Storing the new_segment value in the list segments.
        
    def extend(self):
         self.add_segment(self.segments[-1].position())
        
    def move(self):   # function for snake_move.
            for seg_no in range(len(self.segments) - 1, 0, -1 ):     # Iterating over the list segments in reverse order.
                x = self.segments[seg_no - 1].xcor()                 # Accessing the last element from the segment list and getting its x coordinates value.
                y = self.segments[seg_no - 1].ycor()                 # Accessing the last element from the segment list and getting its y coordinates value.
                self.segments[seg_no].goto(x, y)                     # Setting the coordinates of the current segment to the x and y copordinates values obtained.
            self.head.forward(MOVE_DISTANCE)

    def left(self):     # function for snake_left.
        if self.head.heading() != MOVE_RIGHT:
            self.head.setheading(MOVE_LEFT)
    
    def right(self):    # function for snake_right.        
        if self.head.heading() != MOVE_LEFT:
            self.head.setheading(MOVE_RIGHT)
    
    def up(self):      # function for snake_up.
        if self.head.heading() != MOVE_DOWN:
            self.head.setheading(MOVE_UP)   
        
    def down(self):     # function for snake_down.
        if self.head.heading() != MOVE_UP:
            self.head.setheading(MOVE_DOWN)
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        