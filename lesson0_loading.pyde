"""
 * Load and Display  
 * Images can be loaded and displayed to the screen at their actual size
 * or any other size. 
 *The image file must be in the data folder of the current sketch
 *to load successfully """

def setup():
    size(640, 360)
    global img
     
    #TODO- Write the name of image with the type of file after the e.g "moonlight.jpg"
    
    img = loadImage(" ")  
    noLoop()


def draw():
    #Displays the image at its actual size at point (0,0)
    #TODO- change the position of the big image  
    
    image(img, 0, 0)
    
    # Displays the image at point (0, height/2) at half of its size
        
    image(img, 0, height / 2, img.width / 2, img.height / 2)
    
#TODO- change the parameter to numbers  example : height/2 = > 100 you need to find the real size of the window and image 
#TODO- add another images ; make a collage of different images
#TODO- try using filter() methode to the image. read more about filters here
#https://py.processing.org/reference/filter.html 
 
    
