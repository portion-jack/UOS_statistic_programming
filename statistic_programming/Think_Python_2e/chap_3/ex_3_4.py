def do_twice(func,arg):
    func(arg)
    func(arg)
    return None

def print_twice(arg):
    print(arg)
    print(arg)
    return None

def do_four(func,arg):
    do_twice(func,arg)
    do_twice(func,arg)
    return None
