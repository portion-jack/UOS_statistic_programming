# 3_2_1
def do_twice(f):
    f()
    f()
    return None

def print_spam():
    print("spam")
    return None

do_twice(print_spam)

#3_2_2
def do_twice(f,arg):
    f(arg)
    f(arg)
    return None

def print_twice(arg):
    print(arg)
    print(arg)
    return None

do_twice(print_twice,"spam")

def do_four(f,arg):
    do_twice(f,arg)
    do_twice(f,arg)
    return None