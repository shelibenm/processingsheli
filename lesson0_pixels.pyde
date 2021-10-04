


"""very simple code to use loadPixels(). the output is two pictures in one frame"""
#TODO- load another image find the size of the image and adjust the the window size 

img=loadImage('snow.jpg')
image(img,0,0)
size(600,400) # window size

# TODO-change the halfimage Parameters to fit to the window size
# TODO- you can use print() to see the size parameter in the console
# TODO- see what happened if you change the division value to 3 or 4

halfImage= 600*400 / 2

#iterate over the image pixels
#TODO-Read more about loadPixels() methode in the refernce
loadPixels()
for i in range(floor(halfImage)): 
    pixels[i] = pixels[i + floor(halfImage)]
updatePixels()

 
