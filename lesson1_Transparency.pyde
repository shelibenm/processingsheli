"""
 * Transparency. 
 * 
 * Move the pointer left and right across the image to change
 * its position. This program overlays one image over another 
 * by modifying the alpha value of the image with the tint() function. 
 """

offset = 0
easing = 0.05


def setup():
    size(640, 360)
    global img
    #TODO-load another image
    img = loadImage("moonwalk.jpg")    # Load an image into the program


def draw():
    global offset
    image(img, 0, 0)    # Display at full opacity
    dy = (mouseY - img.height / 2) - offset
    offset += dy * easing
    #TODO- change the second 255 to 255/2 and see what happens
    tint(255, 255)    # Display  opacity
    #TODO-Change the parameter so the picture will move side to side clue:offset dx
    image(img, 0, offset)
    
#TODO-read more about the tint() function
#TODO- make an image, composed from an original image and her more traspaent version
