# Ex1
print("\n -- ex1 --")
def b(z):
    prod = a(z,z)
    print(z,prod)
    return prod

def a(x,y):
    x = x+1
    return x*y

def c(x,y,z):
    total = x+y+z
    square = b(total)**2
    return square

x = 1
y = x +1

print(c(x,y+3,x+y))

# Ex2
print("\n -- ex2 --")
"""
Exercise 2
The Ackermann function, A(m, n), is defined:
"""
def ack(m,n):
    if m == 0 :
        return n+1
    elif (m > 0) & (n == 0):
        return ack(m-1,1)
    elif (m > 0) & (n > 0):
        return ack(m-1,ack(m,n-1))

# Ex3
print("\n -- ex3 --")
"""
A palindrome is a word that is spelled the same backward and forward, like “noon” and “redivider”. Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.

The following are functions that take a string argument and return the first, last, and middle letters:
"""
# 3_1
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

# 3_2
def is_palindrome(string):
    _origin = list(string)
    _reversed = _origin[::-1]
    if _origin == _reversed:
        return True
    elif _origin != _reversed:
        return False
# Ex4
"""
Exercise 4
A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power that takes parameters a and b and returns True if a is a power of b. Note: you will have to think about the base case.
"""
# a가 b의 파워 if a%b ==0
# a/b 가 b의
print("\n --ex4 --")

def is_power(a,b):
    if (a%b==0) & (a/b%b==0):
        return True
    else:
        return False
"""
checker

for i in range(1,10):
    for j in range(1,10):
        print(f"{i},{j} {is_power(i,j)}")
"""

# Ex5
"""
Exercise 5
The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.

One way to find the GCD of two numbers is based on the observation that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). As a base case, we can use gcd(a, 0) = a.

Write a function called gcd that takes parameters a and b and returns their greatest common divisor.

Credit: This exercise is based on an example from Abelson and Sussman’s Structure and Interpretation of Computer Programs.
"""
def gcd(a,b):
    # mk divisor list
    _a_set = list()
    _b_set = list()

    # get divisor
    for i in range(1,a+1):
        if (a%i == 0):
            _a_set.append(i)
    for j in range(1,b+1):
        if (b%j == 0):
            _b_set.append(j)

    # common_divisor
    _common = [x for x in _a_set if x in _b_set]
    _common.sort()
    # get largest common divisor
    return _common[-1]

print(gcd(5,25))
