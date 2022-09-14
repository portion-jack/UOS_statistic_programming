from swampy.TurtleWorld import *

input_len=int(input('length : '))
# input_n = int(input('n : '))
input_angle = float(input('angle : '))


world = TurtleWorld()

#def polygon(t,length=input_len,n=input_n):
#    print(t)
#    for i in range(n):
#        fd(t,length)
#        lt(t,360/n)
#    return None

# polygon(t=Turtle(),length=input_len,n=input_n)

def circle(t,radius=input_len):
    print(t)
    t.delay = 0.01
    for i in range(50):
        fd(t,radius)
        lt(t,360/50)
    return None


def arc(t,radius,angle):
    print(t)
    t.delay = 0.01
    for i in range(50):
        fd(t,radius)
        lt(t,angle/50)
    return None


arc(t=Turtle(),radius=input_len,angle=input_angle)



wait_for_user()
