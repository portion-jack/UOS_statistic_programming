def nested_sum(t):
    ans = 0
    for i in t:
        for j in i:
            ans += j
    return ans

t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))
