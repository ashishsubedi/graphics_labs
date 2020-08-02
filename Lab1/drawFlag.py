import glfw
from OpenGL.GL import *
import numpy as np
from numpy import sin,cos



def circle1(x, y, radius):
    angle = 0.0
    glBegin(GL_POLYGON)
    for i in range(100):
	
        angle = i*2*(np.pi/100)
        glVertex2f(x+(cos(angle)*radius),y+(sin(angle)*radius))
   
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


vertices = np.array([
    #1st quad
    scale*(0.150)+x_offest,scale*(0.330)+y_offset,0,
    scale*(0.132)+x_offest,scale*(0.320)+y_offset,0,
    scale*(0.140)+x_offest,scale*(0.301)+y_offset,0,
    scale*(0.119)+x_offest,scale*(0.307)+y_offset,0,
    scale*(0.110)+x_offest,scale*(0.290)+y_offset,0,
    scale*(0.100)+x_offest,scale*(0.307)+y_offset,0,
    scale*(0.081)+x_offest,scale*(0.301)+y_offset,0,
    scale*(0.087)+x_offest,scale*(0.320)+y_offset,0,
    scale*(0.070)+x_offest,scale*(0.330)+y_offset,0,
    scale*(0.087)+x_offest,scale*(0.339)+y_offset,0,
    scale*(0.081)+x_offest,scale*(0.358)+y_offset,0,
    scale*(0.100)+x_offest,scale*(0.352)+y_offset,0,
    scale*(0.109)+x_offest,scale*(0.370)+y_offset,0,
    scale*(0.119)+x_offest,scale*(0.352)+y_offset,0,
    scale*(0.138)+x_offest,scale*(0.358)+y_offset,0,
    scale*(0.132)+x_offest,scale*(0.359)+y_offset,0,
    scale*(0.132)+x_offest,scale*(0.359)+y_offset,0,
  
],dtype=np.float32)
# vertices = np.array([
#     -0.4,0.85,0,
#     0.4, 0.0, 0,
#     -0.4, 0.0, 0,
#     0.4, -0.7, 0,
#     -0.4, -0.7, 0,
   
# ],dtype=np.float32)


glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3,GL_FLOAT,0,vertices)

glClearColor(0.3,0.3,0.3,.3)

# Main loop
while not glfw.window_should_close(window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    # Draws the shape in red
    # glDrawArrays(GL_POLYGON,0,5)

    glColor3f(1.0,0.,0.)
    glBegin(GL_POLYGON)
    glVertex3f(-0.4,0.85,0)
    glVertex3f(0.4, 0.0, 0)
    glVertex3f(-0.2, 0.0, 0)
   
    glVertex3f(0.5, -0.7, 0)
    glVertex3f(-0.4, -0.7, 0)
    glEnd()

    glColor3f(0.0,0.,1.)
    glLineWidth(10)

    # #Outlines blue border
    glBegin(GL_LINE_LOOP)
    glVertex3f(-0.4,0.85,0)
    glVertex3f(0.4, 0.0, 0)
    glVertex3f(0.09, 0.0, 0)
    glVertex3f(0.5, -0.7, 0)
    glVertex3f(-0.4, -0.7, 0)
    glEnd()
    
    # #Outlines blue border

    # glColor3f(0.1,0.1,0.9)
    # glLineWidth(5)
    # glDrawArrays(GL_LINE_LOOP,0,5)

    #Moon

    glColor3f(1.0,1.0,1.0)
    circle1(-0.1,0.15,0.1)
    glColor3f(1.0,0.0,0.0)
    circle1(-0.1,0.2,0.1)
    glColor3f(1.0,1.0,1.0)
    circle1(-0.1,0.15,0.05)

    #Sun
    x_offest = 0
    y_offset = -1
    scale = 2
    glColor3f(1.0,1.0,1.0)
    glDrawArrays(GL_TRIANGLE_FAN,0, 15)

    glColor3f(1.0,0.0,0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.062,-0.325,0)
    glVertex3f(-0.,-0.45,0)
    glVertex3f(-0.0,-0.23,0)
    glEnd()
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.067,-0.3,0)
    glVertex3f(-0.03,-0.34,0)
    glVertex3f(-0.067,-0.36,0)
    glEnd()
    # glBegin (GL_POLYGON)
    # glVertex3f(scale*(0.20)+x_offest,scale*(0.600)+y_offset,0)
    # glVertex3f(scale*(0.22)+x_offest,scale*(0.630)+y_offset,0)
    # glVertex3f(scale*(0.24)+x_offest,scale*(0.600)+y_offset,0)
    # glVertex3f(scale*(0.26)+x_offest,scale*(0.610)+y_offset,0)
    # glVertex3f(scale*(0.25)+x_offest,scale*(0.585)+y_offset,0)
    # glVertex3f(scale*(0.27)+x_offest,scale*(0.560)+y_offset,0)
    # glVertex3f(scale*(0.25)+x_offest,scale*(0.560)+y_offset,0)
    # glVertex3f(scale*(0.22)+x_offest,scale*(0.530)+y_offset,0)
    # glVertex3f(scale*(0.20)+x_offest,scale*(0.560)+y_offset,0)
    # glVertex3f(scale*(0.16)+x_offest,scale*(0.555)+y_offset,0)
    # glVertex3f(scale*(0.19)+x_offest,scale*(0.580)+y_offset,0)
    # glVertex3f(scale*(0.16)+x_offest,scale*(0.600)+y_offset,0)
    # glEnd()
    

    # glColor3f(1.0,1.0,1.0)
    # circle1(-0.09,-0.4,0.1)


    # glBegin (GL_POLYGON)
   
    # #1st Quadrant  
    # glVertex3f(scale*(0.100)+x_offest,scale*(0.000)+y_offset,0)
    # glVertex3f(scale*(0.070)+x_offest,scale*(0.028)+y_offset,0)
    # glVertex3f(scale*(0.084)+x_offest,scale*(0.056)+y_offset,0)
    # glVertex3f(scale*(0.042)+x_offest,scale*(0.042)+y_offset,0)
    # glVertex3f(scale*(0.056)+x_offest,scale*(0.084)+y_offset,0)
    # glVertex3f(scale*(0.014)+x_offest,scale*(0.070)+y_offset,0)
    # glVertex3f(scale*(0.000)+x_offest,scale*(0.100)+y_offset,0)

    # #4th Quadrant  
    # glVertex3f(scale*(0.100)+x_offest,scale*(-0.000)+y_offset,0)
    # glVertex3f(scale*(0.070)+x_offest,scale*(-0.028)+y_offset,0)
    # glVertex3f(scale*(0.084)+x_offest,scale*(-0.056)+y_offset,0)
    # glVertex3f(scale*(0.042)+x_offest,scale*(-0.042)+y_offset,0)
    # glVertex3f(scale*(0.056)+x_offest,scale*(-0.084)+y_offset,0)
    # glVertex3f(scale*(0.014)+x_offest,scale*(-0.070)+y_offset,0)
    # glVertex3f(scale*(0.000)+x_offest,scale*(-0.100)+y_offset,0)
    # #Reflection along y axis
    # #2nd Quadrant  
    # glVertex3f(scale*(-0.100)+x_offest,scale*(0.000)+y_offset,0)
    # glVertex3f(scale*(-0.070)+x_offest,scale*(0.028)+y_offset,0)
    # glVertex3f(scale*(-0.084)+x_offest,scale*(0.056)+y_offset,0)
    # glVertex3f(scale*(-0.042)+x_offest,scale*(0.042)+y_offset,0)
    # glVertex3f(scale*(-0.056)+x_offest,scale*(0.084)+y_offset,0)
    # glVertex3f(scale*(-0.014)+x_offest,scale*(0.070)+y_offset,0)
    # glVertex3f(scale*(-0.000)+x_offest,scale*(0.100)+y_offset,0)

    # #4th Quadrant  
    # glVertex3f(scale*(-0.100)+x_offest,scale*(-0.000)+y_offset,0)
    # glVertex3f(scale*(-0.070)+x_offest,scale*(-0.028)+y_offset,0)
    # glVertex3f(scale*(-0.084)+x_offest,scale*(-0.056)+y_offset,0)
    # glVertex3f(scale*(-0.042)+x_offest,scale*(-0.042)+y_offset,0)
    # glVertex3f(scale*(-0.056)+x_offest,scale*(-0.084)+y_offset,0)
    # glVertex3f(scale*(-0.014)+x_offest,scale*(-0.070)+y_offset,0)
    # glVertex3f(scale*(-0.000)+x_offest,scale*(-0.100)+y_offset,0)
   

    # glEnd()


    glfw.swap_buffers(window)
    glFlush()

glfw.terminate()
