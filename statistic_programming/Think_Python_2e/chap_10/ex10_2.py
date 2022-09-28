def cumsum(t):
    li_ans = list()
    sum = 0
    for i in t:
        sum += i
        li_ans.append(sum)
    return li_ans

t = [1, 2, 3]
print(cumsum(t))
