# 6_1
def b(z):
    prod = a(z,z)
    print(z,prod)
    return prod

def a(x,y):
    x = x + 1
    return x*y

def c(x,y,z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))

# 6_2

# i = 0
def A(m,n):
    # global i
    # i +=1
    if m == 0 :
        return n+1

    elif (0<m) & (n==0):
        return A(m-1,1)

    elif (0<m) & (0<n):
        return A(m-1,A(m,n-1))
    else:
        print(f"somting wrong\nm={m}, n={n}")

print(A(3,4))
# print(i)

# 6_3
from palindrome import *

print("hello")
print(first("hello"))
print(last("hello"))
print(middle("hello"))
print(middle("hi"))
print(middle("h"))

def is_palindrome(string):
    _initial=list(string)
    _reversed = _initial[::-1]
    if _initial == _reversed:
        return True
    elif _initial != _reversed:
        return False

print(is_palindrome("redivider"))
print(is_palindrome("hello"))

# 6_4
def is_power(a,b):
    if b%a == 0 :
        _ = b//a
        if _%a == 0 :
            return True
        else:
            return False
    else:
        return False

print(is_power(2,8))
print(is_power(3,8))
print(is_power(3,81))

# 6_5

