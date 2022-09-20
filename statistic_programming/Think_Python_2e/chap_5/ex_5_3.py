# a^(n) + b^(n) = c^(n)
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

n = int(input("n = "))
if n =< 2:
    print("not related to fermat prob")
    break


def check_fermat(a=a,b=b,c=c,n=n):
    ans_1 = a**n + b**n
    ans_2 = c**n
    if ans_1 == ans_2:
        print("페르마가 틀렸다!")
    elif ans_1 != ans_2:
        print("아냐, 그건 아니지.")
    return None

check_fermat()
