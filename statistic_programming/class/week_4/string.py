# join with string
print(",".join('abcd'))
print("".join(['a','b','c','d']))

# strip
s = ' hi '
print(s.lstrip())
print(s.rstrip())
print(s.strip())

# split
s_a = 'abcd'
s_b = 'a b c d'

# print(s.split(""))
print(list(s_a))
print(s_b.split())
print(s_b.split(" "))

# in
a = 'hi'
b = 'hello jack'

if a in b:
    print(f"'{a}' is in '{b}'")
elif a not in b:
    print(f"'{a}' is not in '{b}'")

# string _ sort
s_a = 'apple'
s_b = 'banana'

if s_a < s_b:
    print(f"{s_a} comes after than {s_b}")
elif s_b < s_a:
    print(f"{s_a} comes later than {s_b}")
elif s_b == s_a:
    print(f"{s_a} is same with {s_b}")
