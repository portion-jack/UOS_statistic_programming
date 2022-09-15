a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))


def is_triangle(a, b, c):
    _list = [a, b, c]
    _list.sort()
    _len_sum = _list[0] + _list[1]
    _len_long = _list[2]
    if _len_sum <= _len_long:
        print("이것은 삼각형을 만들 수 없습니다.")
    if _len_long < _len_long:
        print("이것은 삼격형이 될 수 있습니다.")


is_triangle(a, b, c)
