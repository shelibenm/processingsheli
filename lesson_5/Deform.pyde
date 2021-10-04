"""
Deform. 

A GLSL version of the oldschool 2D deformation effect, by Inigo Quilez.
Ported from the webGL version available in ShaderToy:
http://www.iquilezles.org/apps/shadertoy/
(Look for Deform under the Plane Deformations Presets)

"""

tex = None
deform = None

def setup():
    global tex, deform
    size(640, 360, P2D)
    textureWrap(REPEAT)
    tex = loadImage("bed.jpg")
    deform = loadShader("deform.glsl")
    deform.set("resolution", float(width), float(height))


def draw():
    deform.set("time", millis() / 1000.0)
    deform.set("mouse", float(mouseX), float(mouseY))
    shader(deform)
    image(tex, 0, 0, width, height)

#TODO-load other image, replace the bed.jpg with the new img. see whats happen
#TODO- read more about the loadshader in the referance
#todo-think of other wayes to use the load shader() and create your own draw function
