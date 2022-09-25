def read_words():
    file = open("word.txt",mode='r')
    strings = file.read()
    strings = strings.replae("\n", " ")
    strings = strings.split(" ")
    for i in strings:
        if len(i) >= 20:
            print(i)
    file.close()

