
barWidth = 1
# TODO-Change The barWidth to 20

def setup():
    #TODO- use the barWidht variable instead of  the number 20
    size(20 * 32, 360)
    colorMode(HSB, width, height, 100)
    noStroke()


def draw():
    #TODO-replace the 1 in the WhichBar variable with the mouseX value
    whichBar = 1 / barWidth
    barX = whichBar * barWidth
    #TODO- replace the number 25 in the fill function with the value "barX"
    #TODO- replace the number 1 in the fill function with "mouseY"
    fill(25, 1, 66)
    rect(barX, 0, barWidth, height)
    
#TODO- Explain: whats the meaning of the variable cald "barX"
#TODO-  read more about sturation effect
#TODO- use the sturation effect on other shape or image
