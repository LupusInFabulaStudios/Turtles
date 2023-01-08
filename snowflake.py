import turtle
import enum
import random

class SnowflakeTypes(enum.Enum):
    Shrink = 0
    Grow = 1
    Stay = 2
    Wild = 3

class Snowflake:
    def __init__(self, position = (0,0)):
        self.turt = turtle.Turtle()
        self.turt.penup()
        self.turt.goto(position)
        self.turt.pendown()

    def DrawBranch(self, length = 100.0, falanges = 4, layers = 2, angle = 45.0, multiplier = 0.5, falanges_dist = 0.5, type = SnowflakeTypes.Stay):
        
        t = self.turt
        t.speed(0)

        f_length = length * falanges_dist

        if(layers == 0):
            t.forward(length)
            t.back(length)
            return
        else:
            t.forward(f_length)
        
        interfalanges_dist = (length - f_length) / falanges

        n_length = length
        for i in range(falanges):
            #the version of python I'm using doesn't support
            #switch statements :( so this will have to do
            t.right(angle)
            self.DrawBranch(n_length * multiplier, round(falanges * multiplier) + 1, layers - 1, angle, multiplier, falanges_dist, type)
            t.left(angle * 2)
            self.DrawBranch(n_length * multiplier, round(falanges * multiplier) + 1, layers - 1, angle, multiplier, falanges_dist, type)
            t.right(angle)
            t.forward(interfalanges_dist)
            if(type == 0):
                n_length *= multiplier / 2
            elif(type == 1):
                n_length /= multiplier
            elif(type == 3):
                if(random.random() > .5):
                    n_length *= multiplier / 2
                else:
                    n_length /= multiplier
        
        t.penup()
        t.back(length)
        t.pendown()



    def DrawFlake(self, branches = 5, length = 10, multiplier = .5, layers=2, type = SnowflakeTypes.Stay):
        for i in range(branches):
            a = 360.0 / branches
            self.DrawBranch(falanges=round(branches / 2),length=length,angle=a, falanges_dist=.6, multiplier=multiplier, layers=layers)
            self.turt.right(a)