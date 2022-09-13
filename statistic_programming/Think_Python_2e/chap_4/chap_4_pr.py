from swampy.TurtleWorld import *

# world = TurtleWorld()
# bob = Turtle()
#
# print(bob)
#
#
# for i in range(4):
#     fd(bob,100)
#     lt(bob)

world = TurtleWorld()
def square(t):
    # world = TurtleWorld()
    print(t)
    for i in range(4):
        fd(t,100)
        lt(t)
    return None

t = Turtle()
square(t)

wait_for_user()
