print("+","-","-","-","-","+","-","-","-","-","+")
print("|"," "," "," "," ","|"," "," "," "," ","|")
print("|"," "," "," "," ","|"," "," "," "," ","|")
print("|"," "," "," "," ","|"," "," "," "," ","|")
print("|"," "," "," "," ","|"," "," "," "," ","|")
print("+","-","-","-","-","+","-","-","-","-","+")
print("|"," "," "," "," ","|"," "," "," "," ","|")
print("|"," "," "," "," ","|"," "," "," "," ","|")
print("|"," "," "," "," ","|"," "," "," "," ","|")
print("|"," "," "," "," ","|"," "," "," "," ","|")
print("+","-","-","-","-","+","-","-","-","-","+")

def print_a_1():
    print("+",end=" ")
    return None

def print_a_2():
    print("+")
    return None

def print_c_1():
    print("-",end=" ")
    return None

def print_b_1():
    print("|",end=" ")
    return None

def print_b_2():
    print("|")
    return None

def print_d_1():
    print(" ",end=" ")
    return None

def do_twice(f):
    f()
    f()
    return None

def do_four(f):
    do_twice(f)
    do_twice(f)
    return None

def line_1():
    print_a_1()
    do_four(print_c_1)
    print_a_1()
    do_four(print_c_1)
    print_a_2()
    return None
def line_2():
    print_b_1()
    do_four(print_d_1)
    print_b_1()
    do_four(print_d_1)
    print_b_2()
    return None

line_1()
do_four(line_2)
line_1()
do_four(line_2)
line_1()


def line_1_ver2():
    print_a_1()
    do_four(print_c_1)
    print_a_1()
    do_four(print_c_1)
    print_a_1()
    do_four(print_c_1)
    print_a_1()
    do_four(print_c_1)
    print_a_2()
    return None
def line_2_ver2():
    print_b_1()
    do_four(print_d_1)
    print_b_1()
    do_four(print_d_1)
    print_b_1()
    do_four(print_d_1)
    print_b_1()
    do_four(print_d_1)
    print_b_2()
    return None

line_1_ver2()
do_four(line_2_ver2)
line_1_ver2()
do_four(line_2_ver2)
line_1_ver2()
do_four(line_2_ver2)
line_1_ver2()
do_four(line_2_ver2)
line_1_ver2()

