import glfw


# Raise exception if not initialized
if not glfw.init():
    raise Exception("GLFW cannot be initialized")

# Create GLFW window handle
window = glfw.create_window(640, 480, "Lab 1", None, None)
# If failed, terminate and raise exception
if not window:
    glfw.terminate()
    raise Exception("GLFW window cannot be creted")
# Set current position to specified position
glfw.set_window_pos(window, 400, 200)
# Create the context for the window
glfw.make_context_current(window)


print(glfw.get_window_size(window))
# Main loop
while not glfw.window_should_close(window):
    glfw.poll_events()
   
    glfw.swap_buffers(window)

glfw.terminate()
