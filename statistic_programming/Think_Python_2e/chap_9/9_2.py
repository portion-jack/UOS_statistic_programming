def has_no_e(w) -> bool:
    for i in w:
        if i == 'e':
            return False
    return True

file = open('words.txt',mode='r')

strings = file.read()
strings = strings.replace("\n"," ")
strings = strings.split(" ")

counts = 0
for word in strings:
    if has_no_e(word):
        print(word)
        counts += 1

print(f"percentage of no e {counts/len(strings)}")

