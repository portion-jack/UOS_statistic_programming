def uses_only(w,s):
    w = w + " "
    if set(w) == set(s):
        return True
    return False
