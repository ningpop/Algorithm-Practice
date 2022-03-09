# 동전들을 가지고 value를 만들어낼 수 있는지 확인하는 함수
def greedy(coin: list, value: int) -> bool:
    for i in coin: # 동전 리스트 순회
        if value >= i: # 해당 동전이 value보다 작거나 같은 경우 포함 가능
            value -= i # 해당 동전의 가치에서 value를 빼기
    
    if value == 0: # value가 0이 됨으로써 동전으로 value를 만들 수 있다면
        return True
    return False

N = int(input())
coin = list(map(int, input().split()))

coin.sort(reverse=True) # 큰 액면가의 동전부터 순회할 예정이므로 내림차순 정렬

result = 1 # 만들 수 없는 최소값을 찾기 위해서는 작은 값부터 증가하며 찾기
while True:
    if greedy(coin, result): # 동전들로 값을 만들 수 있는지 확인
        result += 1 # 다음 최소값으로 넘어가기
        continue
    else: # 만들 수 없으면 원하는 값 찾음
        break

print(result)