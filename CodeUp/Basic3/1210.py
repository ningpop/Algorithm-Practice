menu = {1:400, 2:340, 3:170, 4:100, 5:70}
food = list(map(int, input().split()))
result = 0
for i in food:
    result += menu[i]
if result > 500:
    print('angry')
else:
    print('no angry')