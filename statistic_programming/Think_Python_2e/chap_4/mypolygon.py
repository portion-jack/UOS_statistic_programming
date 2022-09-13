from swampy.TurtleWorld import *


world = TurtleWorld()

def square(t):

    print(t)
    for i in range(4):
        fd(t, 100)
        lt(t)
    return None


square(Turtle())

wait_for_user()
