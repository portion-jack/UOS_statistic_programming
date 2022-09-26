from read_words import *
li_w = read_words()

def is_abecedarian(w):
    l_w = list(w)
    sorted_lw = l_w.copy()
    sorted_lw.sort()
    if l_w == sorted_lw:
        return True
    else:
        return False

count = 0
for w in li_w:
    if is_abecedarian(w):
        print(w)
        count += 1
print(f"{count} / {len(li_w)}")
