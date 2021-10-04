"""
Milliseconds. 

A millisecond is 1/1000 of a second. 
Processing keeps track of the number of milliseconds a program has run.
By modifying this number with the modulo(%) operator, 
different patterns in time are created.  
"""

#TODO-run the code for 1 minute
def setup():
    global scale
    size(640, 360)
    noStroke()
    #TODO-change the scale value to get thiner bars
    scale = width / 10


def draw():
    for i in range(0, scale, 1):
       
        colorMode(RGB, (i + 1) * scale * 10)
        #TODO-change the operators in the fill() to  lower or higher[e.g change the 10 to 2]
        #values-whats happen?
        fill(millis()% ((i + 1) * scale * 10))
        rect(i * scale, 0, scale, height)
#TODO-find a way to change the color from gray to red or blue
#while using the millis() methode
#TODO-replace the % with [/]division or multiply [*] sign -whats the differance?
#TODO-create your own function using the millis() to get interesting patterns
