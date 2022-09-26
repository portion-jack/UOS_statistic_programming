def check_words():
    file = open("word.txt",mode='r')
    strings = file.read()
    strings = strings.replae("\n", " ")
    strings = strings.split(" ")
    for i in strings:
        if len(i) >= 20:
            print(i)
    file.close()

def read_words():
    file = open('words.txt',mode='r')
    strings = file.read()
    strings = strings.replace("\n", " ")
    li_string = strings.split(" ")
    return li_string
