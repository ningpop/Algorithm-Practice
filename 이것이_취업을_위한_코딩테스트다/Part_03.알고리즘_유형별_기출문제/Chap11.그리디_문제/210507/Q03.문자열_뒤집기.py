'''
# 오답
S = input()

result = 0
for idx, val in enumerate(S):
    if val != S[idx-1]:
        result += 1

print(result//2)
'''

S = input()

result = 0
for i in range(len(S)-1): # 1 작은 리스트 길이로 순회하도록 하여
    if S[i] != S[i+1]: # 현재 index의 값과 다음 index의 값을 비교
        result += 1 # 패턴 생성

print((result+1)//2) # 0과 1 선택지를 가지기에 뒤집는 방법 수는 2로 나눈 몫