
# image size is very important also the image should not be risized or compressed
# use an original small image for this excersize

img=loadImage("interlock.jpg")
println([img.width,img.height])

def setup():   
    global img
    img=loadImage('interlock.jpg')
    size(225,225) # size of window >= size of image use img.width;img.height
    img.loadPixels()
    loadPixels()
    
def draw():    
    for x in range(img.width):
        for y in range(img.height):
    
            # Calculate the 1D of pixel location
            loc = x+ y*img.width
            #Get the R,G,B values from each image-pixel
            r,g,b =   0,0,0
            r = red  (img.pixels[loc])
            g = green(img.pixels[loc])
            b = blue (img.pixels[loc])
            # Get the distance from mouse coordinate
            distance =dist(x,y,mouseX,mouseY)
            maxdist = 50
            # use map methode to define the "flashlight" radius and brightness
            # if the pixel is too far the brightness be close to 0.0 if it is in the range
            # brightness will be close to 1.0
            
            #TODO-replace the adjustBrightness with this formula 255*(maxdist-distance)/maxdistance 
            #and try to understand the different approuch
            #TODO-change the map() value to get larger light radius[light more pixels]
            adjustBrightness = map(distance,0,maxdist,3,0)
            
            r *=  adjustBrightness
            g *=  adjustBrightness
            b *=  adjustBrightness
            #TODO- read about constrain methode
            r=constrain(r,0,255)
            g=constrain(g,5,255)
            b=constrain(b,5,255)
                    
            c = color(r,g,b)
            pixels[y * width +x]=c
    updatePixels()     
#TODO-read more about the pixels methode in the refernces
