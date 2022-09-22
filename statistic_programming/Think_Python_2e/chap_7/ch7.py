# Ex1
"""
Exercise 1
Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt that takes a as a parameter, chooses a reasonable value of x, and returns an estimate of the square root of a.
"""

def mysqrt(a,x=3):
    while True:
        #print(x)
        y = (x+a/x) / 2
        epsilon = 1e-5
        if abs(y-x) < epsilon:
            break
        x = y
    return x

import math

def test_square_root():
    print("a    mysqrut(a)  math.sqrt(a)    diff")
    print("-    ----------  ------------    ----")
    for i in range(1,10):
        print(f"{i:.3f}     {mysqrt(i,3):.3f}   {math.sqrt(i):.3f}           {abs(mysqrt(i,3)-math.sqrt(i)):.10f}")
    return None

# test_square_root()

# Ex2
"""
Exercise 2
The built-in function eval takes a string and evaluates it using the Python interpreter. For example:

Write a function called eval_loop that iteratively prompts the user, takes the resulting input and evaluates it using eval, and prints the result.

It should continue until the user enters 'done', and then return the value of the last expression it evaluated.
"""
def eval_loop():
    while True:
        _input = input("입력 : \n")
        if _input == "done":
            break
        print(eval(_input))
    return None
eval_loop()

# Ex3

