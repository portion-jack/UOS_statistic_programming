def is_sorted(t):
    _ = t.copy()
    _.sort()
    if t == _:
        return True
    if t != _:
        return False

print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))
