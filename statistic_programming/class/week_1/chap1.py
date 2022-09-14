print("Hello, World!")

def killo2mile(killo):
    mile = killo/1.61
    return mile

def per_hour(length,hours,minutes,seconds):
    time = hours + minutes/60 + seconds/3600
    velocity = length / time
    return velocity

mile = killo2mile(10)
ans = per_hour(mile,0,43,30)
print(ans)
