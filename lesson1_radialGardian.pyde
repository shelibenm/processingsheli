"""
Radial Gradient. 

Draws a series of concentric circles to create a gradient 
from one color to another.
"""


def setup():
    size(640, 360)
    background(0)
#TODO-Change the colormode to HSB see  whats happend
    colorMode(RGB, 256, 100, 100)
    noStroke()
    ellipseMode(RADIUS)
    frameRate(1)


def draw():
    background(0)
    for x in range(0, width + 1, width / 2):
        drawGradient(x, height / 2)


def drawGradient(x, y):
    # TODO-add more ellipes to the img clue: change the radius to 4 or more
    radius = width / 1
    #TODO-Change the range to 360 to fit the HSB color mode
    h = random(0, 256)
    for r in range(radius, 0, -1):
        fill(h, 90, 90)
        ellipse(x, y, r, r)
        #TODO- Change the mod to 360 
        h = (h + 1) % 256
        
#TODO-read more about colormode in the refernce
#TODO-Create another drawGradient using other x, y values
