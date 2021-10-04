
#TODO-run the code-see whats happen
def setup():
    size(480,270)
def draw():
    background(255)
    stroke(0)
    line(240,0,240,360)
    line(0,135,640,135)
#fill a black color
    noStroke()
    fill(0)
    #Depending on the mouse location, a different rectangle is displayed.
    if (mouseX < 240 and mouseY < 135):
        rect(0, 0, 240, 135)
    elif (mouseX > 240 and mouseY < 135): 
        rect(240, 0, 240, 135)
    elif (mouseX < 240 and mouseY > 135): 
        rect(0, 135, 240, 135)
    elif (mouseX > 240 and mouseY > 135): 
        rect(240, 135, 240, 135)
  
#TODO-add another condition which create fifth rectangle in the middle 
#TODO-change the texture or th color of the flliping rectangle[like a card]
