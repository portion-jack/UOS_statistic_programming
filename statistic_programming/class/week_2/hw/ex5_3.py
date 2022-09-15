a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))
n = int(input("n :"))

if n <= 2 :
    print("그건 페르마의 정리와 무관한데,\n진행?")
    ans=input("진행 (y/n)")
    if ans != "y":
        raise ValueError



def check_fermat(a, b, c, n):
    _ans1 = a ** n + b ** n
    _ans2 = c ** n
    if _ans1 == _ans2:
        print("페르마가 틀렸다.")
    elif _ans1 != _ans2:
        print("아냐, 그건아니지.")


check_fermat(a, b, c, n)
