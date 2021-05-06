# 모험가 목록에서 해당 값을 모두 삭제한 리스트를 반환하는 함수
def remove_value(l: list, v: int) -> list:
    return [i for i in l if i != v]

n = int(input())
mohumga = list(map(int, input().split()))

answer = 0
while True:
    group = min(mohumga) # 현재 상태에서 공포도가 가장 낮은 모험가를 선택(기준 모험가)
    
    mohumga_count = 0 # 해당 모험가와 같은 그룹에 들어갈 수 있는 모험가의 수
    for i in mohumga:
        if group >= i: # 모험가의 공포도가 기준 모험가의 공포도보다 낮다면
            mohumga_count += 1 # 같은 그룹이 가능한 모험가 수 +1
    
    # (기준 모험가의 공포도) <= (해당 모험가보다 작거나 같은 공포도를 가진 모험가 수) 일때
    # 그룹 생성 가능
    if group <= mohumga_count:
        answer += (mohumga_count//group) # 그룹 수 증가

    mohumga = remove_value(mohumga, group) # 모험가 목록에서 기준 모험가들을 모두 삭제

    if not mohumga: # 모험가 목록이 비었다면 종료
        break

print(answer)