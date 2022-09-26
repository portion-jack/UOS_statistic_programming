file = open('words.txt',mode='r')
s = file.read()
s = s.replace("\n"," ")
li_s = s.split(" ")

def uses_only(w,s):
    w = w + " "
    for _ in list(set(s)):
        if _ in w:
            pass
        else:
            return False
    return True

count = 0
for i in li_s:
    if uses_only("acefhlo",i):
        print(i)
        count += 1

print(f"{count} / {len(li_s)}")
