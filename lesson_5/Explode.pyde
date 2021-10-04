"""
Explode
by Daniel Shiffman.

Mouse horizontal location controls breaking apart of image and
maps pixels from a 2D image into 3D space. Pixel brightness controls
translation along z axis.
"""

#TODO-run the code. replace the image see if the effect isthe same
def setup():
    size(640, 360, P3D)
    # Number of columns and rows in our system
    global columns, rows, cellsize, img
    img = loadImage("eames.jpg")  # Load the image
    
    #TODO-ChangeTHe cellsize to 10.see whats happen
    cellsize = 2  # Dimensions of each cell in the grid
    columns = img.width / cellsize  # Calculate # of columns
    rows = img.height / cellsize  # Calculate # of rows

def draw():
    background(0)
    # Begin loop for columns
    for i in range(columns):
        # Begin loop for rows
        for j in range(rows):
            
            #TODO-comment the next two lines of x and y and replace the i and j 
            #with x and y -see whats the diffrence
            
            x = i * cellsize + cellsize / 2  # x position
            y = j * cellsize + cellsize / 2  # y position
            loc = x + y * img.width  # Pixel array location
            c = img.pixels[loc]  # Grab the color
            # Calculate a z position as a function of mouseX and pixel
            # brightness
            z = (mouseX / float(width)) * brightness(img.pixels[loc]) - 20.0
            
            
            # Translate to the location, set fill and stroke, and draw the rect
            with pushMatrix():
                #TODO-write your own translate function-this is p3d mode
                # change the mode to P2D in the setup and run-is it working?why?
                translate(x + 200, y + 100,z)
                fill(c, 204)
                noStroke()
                rectMode(CENTER)
                rect(0, 0, cellsize, cellsize)
