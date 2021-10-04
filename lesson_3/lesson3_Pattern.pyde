"""
Patterns. 

Move the cursor over the image to draw with a software tool 
which responds to the speed of the mouse. 
"""


def setup():
    size(640, 360)
    background(102)


def draw():
    # Call the variableEllipse() method and send it the
    # parameters for the current mouse position
    # and the previous mouse position
    variableEllipse(mouseX, mouseY, pmouseX, pmouseY)

# The simple method variableEllipse() was created specifically
# for this program. It calculates the speed of the mouse
# and draws a small ellipse if the mouse is moving slowly
# and draws a large ellipse if the mouse is moving quickly.


def variableEllipse(x, y, px, py):
    speed = abs(x- px) + abs(y - py)
    stroke(speed)
    fill(123,145,120)
    ellipse(x, y, speed, speed)
#TODO-change the speed variable so the effect will be reversed [small ellipse when the
# mouse moving fast  and vise versa - what is the pattern?
#TODO- try to create your own speed variable / value for the ellipse size in accordence
# to movement                                                             
