t = [1, 2, 3, 4]

def chop():
    global t
    t = t[1:-1]
    return None

chop()
print(t)
