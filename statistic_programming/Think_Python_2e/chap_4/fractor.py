from swampy.TurtleWorld import *


world = TurtleWorld()

def draw(t,length,n):
    t.delay = 0.01
    if n==0:
        return None
    angle = 50
    fd(t,length*n)
    lt(t,angle)
    draw(t,length,n-1)
    rt(t,2*angle)
    draw(t,length,n-1)
    lt(t,angle)
    bk(t,length*n)
    return None


draw(t=Turtle(),length=5,n=10)
