"""
Iteration.

Iteration with a "for" structure to construct repetitive forms. 
"""

num = 14

size(640, 360)
background(102)
noStroke()

# Draw gray bars
#TODO- run the code and try to understand the connction between the input and output
#TODO-change the range number with another value
fill(255)
y = 60
for i in range(num / 3):
    rect(50, y, 475, 10)
    y += 20

# Gray bars
fill(51)
y = 40
for i in range(num):
    rect(405, y, 30, 10)
    y += 20
#TODO- try to change the y value to create horizontal[from side to side]patterns
y = 50
for i in range(num):
    rect(425, y, 30, 10)
    y += 20

# Thin lines
#TODO- fill/replace the values of range, rect() and Y to create
# thin lines ordered from top to bottom
y = 45
fill(0)
for i in range(0):
    rect(0,0,0,0)
    y += 0
#TODO-write your own for loop and use different shapes and colors
