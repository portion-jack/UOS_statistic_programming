from read_words import *
li_w = read_words()


def uses_all(w,s):
    li_s = list(s)
    for _ in li_s:
        if _ in w:
            pass
        else:
            return False
    return True
count = 0
for w in li_w:
    if uses_all(w,"vowelsae"):
        print(w)
        count += 1
print(f"{count}/{len(li_w)}")
