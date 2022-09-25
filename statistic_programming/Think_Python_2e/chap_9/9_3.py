def avoids(w,s) -> bool:
    if w in s:
        return False
    return True

print(avoids('hi','hi my name is jack'))
print(avoids('jack','hi my name is john'))


