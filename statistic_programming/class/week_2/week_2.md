# chap3 함수

## 가변인자

def make_pizza(*toppings):
    print("\nMaking a pizza with the followings")
    for topping in toppings:
        print("- "+topping)
make_pizza("peperoni","green peppers","chicken")

## dict로 인자를 받기
def print_kwargs(**kewargs):
    return None

## 재귀함수
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

>>> factorial(5)
120

