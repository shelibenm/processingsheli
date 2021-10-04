"""
Recursion. 

A demonstration of recursion, which means functions call themselves. 
Notice how the drawCircle() function calls itself at the end of its block. 
It continues to do this until the variable "level" is equal to 1. 
"""

#TODO-run the code-

def setup():
    size(640, 360)
    noStroke()
    noLoop()

#TODO-add more circles-change the number of levels
def draw():
    drawCircle(width / 2, 280, 6)


def drawCircle(x, radius, level):
    tt = 126 * level / 4.0
    fill(tt)
    ellipse(x, height / 2, radius * 2, radius * 2)
    if level > 1:
        #TODO-try to make less recursion cycles by changing the level value
         #for example level= level -2       
        level = level - 1
        drawCircle(x - radius / 2, radius / 2, level)
        drawCircle(x + radius / 2, radius / 2, level)
#TODO-add more recursion function for example:drawrect()that create diagmol pattern
#not horizontal like the drawCircle() above
#
