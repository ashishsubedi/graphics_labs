import glfw
from OpenGL.GL import *
import numpy as np
from numpy import sin,cos,pi

def circle1(x, y, radius):
    angle = 0.0
    glBegin(GL_POLYGON)
    for i in range(100):
	
        angle = i*2*(np.pi/100)
        glVertex2f(x+(cos(angle)*radius),y+(sin(angle)*radius))
   
    glEnd()

def drawSun(scaleX,scaleY,x,y):
 
        

    glBegin(GL_TRIANGLES)
    glVertex2f(x+scaleX* 0.000, y+scaleY*0.100)
    glVertex2f(x+scaleX* 0.0866,y+scaleY*-0.050)
    glVertex2f(x+scaleX*-0.0866, y+scaleY*-0.050)


    glVertex2f(x+scaleX* 0.000,y+scaleY*-0.100)
    glVertex2f(x+scaleX* 0.087,y+scaleY*0.049)
    glVertex2f(x+scaleX*-0.085,y+scaleY*0.049)
    
    glVertex2f(x+scaleX* -0.099, y+scaleY*0.0)
    glVertex2f(x+scaleX* 0.05,y+scaleY*-0.080)
    glVertex2f(x+scaleX* 0.05, y+scaleY*0.086)


    glVertex2f(x+scaleX* 0.1,y+scaleY* -0.000)
    glVertex2f(x+scaleX*-0.049,y+scaleY*0.086)
    glVertex2f(x+scaleX*-0.049,y+scaleY*-0.086)

    glEnd()

# Raise exception if not initialized
if not glfw.init():
    raise Exception("GLFW cannot be initialized")

# Create GLFW window handle
window = glfw.create_window(1280, 720, "Lab 1", None, None)
# If failed, terminate and raise exception
if not window:
    glfw.terminate()
    raise Exception("GLFW window cannot be creted")
# Set current position to specified position
glfw.set_window_pos(window, 400, 200)
# Create the context for the window
glfw.make_context_current(window)

x_offest = -.32
y_offset = -.99
scale = 2

glClearColor(0.3,0.3,0.3,.3)

# Main loop
while not glfw.window_should_close(window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    # Draws the shape of in red

    glColor3f(1.0,0.,0.)
    glBegin(GL_POLYGON)
    glVertex3f(-0.4,0.85,0)
    glVertex3f(0.4, 0.0, 0)
    glVertex3f(-0.2, 0.0, 0)
    glVertex3f(0.5, -0.7, 0)
    glVertex3f(-0.4, -0.7, 0)
    glEnd()

    #Outlines blue border
    glColor3f(0.0,0.,1.)
    glLineWidth(15)

    glBegin(GL_LINE_LOOP)
    glVertex3f(-0.4,0.85,0)
    glVertex3f(0.4, 0.0, 0)
    glVertex3f(0.09, 0.0, 0)
    glVertex3f(0.5, -0.7, 0)
    glVertex3f(-0.4, -0.7, 0)
    glEnd()
    

    moonScaleX = 0.5
    moonScaleY = .5
    moonX = -0.1
    moonY = 0.12

    #Moon

    glColor3f(1.0,1.0,1.0)
    circle1(-0.1,0.15,0.1)
    glColor3f(1.0,0.0,0.0)
    circle1(-0.1,0.2,0.1)
    glColor3f(1.0,1.0,1.0)
    drawSun(moonScaleX,moonScaleY,moonX,moonY)


    #Sun
  
    sunScaleX = 1
    sunScaleY = 1
    sunX = -0.1
    sunY = -0.4

    glColor3f(1.0,1.0,1.0)

    drawSun(sunScaleX,sunScaleY,sunX,sunY)
  
   



    glfw.swap_buffers(window)
    glFlush()

glfw.terminate()


