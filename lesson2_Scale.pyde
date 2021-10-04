"""
Scale
by Denis Grutze.

Paramenters for the scale() function are values specified
as decimal percentages. For example, the method call scale(2.0)
will increase the dimension of the shape by 200 percent.
"""

a = 0.0

def setup():
    size(640, 360)
    noStroke()
    rectMode(CENTER)
    frameRate(30)

def draw():
    global a
    background(102)
    #TODO- change The a paramter to some constant value of angle between 0-360
    #see whats happen example a= 30 a = 220
    a = a + 0.04
    s = cos(a) * 2

    translate(width / 2, height / 2)
    scale(s)
    fill(51)
    rect(0, 0, 50, 50)
    

    translate(75, 0)
    fill(255)
    scale(s)
    rect(0, 0, 50, 50)
    #TODO- add image or othet object and define there zoom-scaling variable
    #use the rect() examples as a model to write your code
