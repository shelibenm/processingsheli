"""
Load and Display a Shape. 
Illustration by George Brower. 

The loadShape() command is used to read simple SVG (Scalable Vector Graphics)
files and OBJ (Object) files into a Processing sketch. This example loads an
SVG file of a monster robot face and displays it to the screen. 
"""

def setup():
    size(640, 360)
    # The file "bot1.svg" must be in the data folder
    # of the current sketch to load successfully
    
    global bot
    #TODO- load other svg file you can create yor own svg, using any graphic tool
    bot = loadShape("bot1.svg")


def draw():
    background(102)
    # Draw at coordinate (110, 90) at size 100 x 100
    #TODO-change the global bot to other name
    #TODO-replace the variable bot with the new name
    shape(bot, 110, 90, 100, 100)
    # Draw at coordinate (280, 40) at the default size
    shape(bot, 280, 40)
    #TODO- Add more svg or shape to your image use the shape-scatch tool in the tools category
    #TODO-add smaller bot/ other shape use scale()function scale paramter range 0-1    
    #TODO- add function that controls the size with x mouse movement
    
