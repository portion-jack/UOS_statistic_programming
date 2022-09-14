# chap3 함수

## 가변인자

def make_pizza(*toppings):
    print("\nMaking a pizza with the followings")
    for topping in toppings:
        print("- "+topping)
make_pizza("peperoni","green peppers","chicken")
