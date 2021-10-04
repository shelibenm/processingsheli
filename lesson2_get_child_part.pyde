"""
Get Child. 

SVG files can be made of many individual shapes. 
Each of these shapes (called a "child") has its own name 
that can be used to extract it from the "parent" file.
This example loads a map of the United States and creates
two PShape objects by extracting the data from two states.
"""

#TODO-search for svg file on line. download it to  the data folder
#in the directory of the processing file. you can create your own svg file
#for example https://emoji-maker.flat-icons.com/ or use the files in the data folder
#TODO-find the names of the parts in the browser inspect option

def setup():
    size(640, 360)
    #TODO- name three global variables: whole,part,part2[you can name it any way you like]
    #example:usa, michigan, ohio and write them in the next line next to 'global'
    global           #put here the three variables
    #TODO- enter the name of file in the bracket loadShape()
    whole = loadShape("")
    #TODO- write the name of the parts inside the getChild() 
    part =  whole.getChild("")
    part2 = whole.getChild("")

def draw():
    background(255)

    # Draw the full map
    shape(whole, -600, -180)

    # Disable the colors found in the SVG file
    part.disableStyle()
    # TODO-Set our own coloring
    fill(0, 0, 0)
    noStroke()
    # Draw a single state
    shape(part, -600, -180)  # 

    # Disable the colors found in the SVG file
    part2.disableStyle()
    
    #TODO- Set our own coloring use rgb methode 
    fill(0, 0, 0)
    noStroke()
    # Draw a single state
    shape(part2, -600, -180)    # 
