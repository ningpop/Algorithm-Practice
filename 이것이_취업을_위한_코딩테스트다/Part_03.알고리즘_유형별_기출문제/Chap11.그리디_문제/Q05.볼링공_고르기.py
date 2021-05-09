from itertools import combinations # combinations 사용

N, M = map(int, input().split())
bowling = list(map(int, input().split()))

comb = list(combinations(bowling, 2)) # combinations를 사용해 주어진 배열을 조합한다.
result = [ (i, j) for i, j in comb if i != j ] # 서로 무게가 다른 공을 골라야한다.
print(len(result))