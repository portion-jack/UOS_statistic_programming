import random

score = 0
iter = 0
while True:
    iter += 1
    numbers = [random.randint(1,100) for i in range(2)]
    operation = random.choice(["+","-"])
    print(numbers[0],operation,numbers[1],'= ?')
    prob = str(numbers[0])+operation+str(numbers[1])
    answer=input('ans : ')
    if answer =="done":
        break
    elif answer == str(eval(prob)):
        score += 1
        print('정답')
    elif answer != str(eval(prob)):
        print('오답')
print(f'점수는 {int((score/iter)*100)}')
