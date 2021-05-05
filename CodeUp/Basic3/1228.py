h, w = map(float, input().split())
pri_w = (h - 100)*0.9
bmi = (w - pri_w)*100/pri_w

if bmi > 20:
    print('비만')
elif 10 < bmi <= 20:
    print('과체중')
else:
    print('정상')