# 서울시립대학교 (2022_02)
## 고급통계프로그래밍

###idea1
- used to
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

-  better
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int,a))
print(a)
