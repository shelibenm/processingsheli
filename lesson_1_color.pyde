"""
Color Variables (Homage to Albers). 

This example creates variables for colors that may be referred to 
in the program by a name, rather than a number. 
"""
size(640, 360)
noStroke()
background(51, 0, 0)
#TODO- change the color of the inside, middle
inside = color(204, 102, 0)
middle = color(204, 153, 0)
#TODO- add three RGB numbers Between 0-255 for the outside color Variable
outside = color()
# These statements are equivalent to the statements above.
# Programmers may use the format they prefer.
#inside = 0xCC6600
#middle = 0xCC9900
#outside = 0x993300
# TODO- translate the outside rect to postion 40,40
with pushMatrix():
    translate(80, 80)
    fill(outside)
    rect(0, 0, 200, 200)
    fill(middle)
    rect(40, 60, 120, 120)
#TODO-Change the scale of the inner rectangle
    fill(inside)
    rect(60, 90, 80, 80)  
#TODO- fill the missing prameters for the second rectangle
with pushMatrix():
    translate()
    fill(inside)
    rect()
    fill(outside)
    rect()
    fill(middle)
    rect()
# TODO- create anothe composion of shape using the pushMatrix() function and translate 
# TODO-read more about pushMatrix() in the references
