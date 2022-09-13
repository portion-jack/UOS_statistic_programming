from swampy.TurtleWorld import *

input_len=int(input('length : '))
input_n = int(input('n : '))

world = TurtleWorld()

def polygon(t,length=input_len,n=input_n):
    print(t)
    for i in range(n):
        fd(t,length)
        lt(t,360/n)
    return None

polygon(t=Turtle(),length=input_len,n=input_n)

wait_for_user()
