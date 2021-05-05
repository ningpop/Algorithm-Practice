lotto = list(map(int, input().split()))
bonus = lotto.pop()

juhee = list(map(int, input().split()))
correct = 0
bonus_correct = 0
for i in juhee:
    if i in lotto:
        correct += 1
    elif i == bonus:
        bonus_correct += 1

if correct == 6:
    print(1)
elif correct == 5:
    if bonus_correct == 1:
        print(2)
    else:
        print(3)
elif correct == 4:
    print(4)
elif correct == 3:
    print(5)
else:
    print(0)