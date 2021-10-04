rotation = 1 
stepSize = 10

def setup() :
  size(800, 800)
 

def draw():
  #global rotation,stepSize
  background(255)
  strokeWeight(2)
  fill(255, 0, 0)
  rect(100, 100, 300, 300)
  fill(0, 96, 255)
  rect(100, 400, 300, 300)
  fill(255, 240, 0)
  rect(400, 100, 300, 300)
  fill(0, 255, 0)
  rect(400, 400, 300, 300)
  strokeWeight(20)
  
  dialarm()  
  if mousePressed:
    play()
    redraw()

def play():
   global rotation, stepSize
   # TODO-try adjusting the random range values of step size 
   #and explor the outcome 
   stepSize = random(5,10)
   if (stepSize > 0):
     rotation += stepSize
     stepSize -= 0.05
     return rotation, stepSize
 
def dialarm():
    pushMatrix()
    translate(400, 400)
    
    #TODO- add millis() function to the rotation and see whats happend 
    #exmple:  rotate(millis() * radians(rotation))
    
    rotate( radians(rotation))
    line(0, 0, 100, 100)
    popMatrix()
#TODO-add text/number/image to each rectangle to indicate differant value to each
# squer and make it like an interactive chance game
