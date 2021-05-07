def solution(d, budget):
    d.sort() # 배열 정렬(작은 신청 금액 부서부터 시작)
    answer = 0
    for i in d: # 작은 신청 금액 부서부터 시작
        if budget >= i: # 예산보다 신청금액이 작거나 같다면
            budget -= i # 예산에서 빼기
            answer += 1 # 지원 부서 수 +1
        else: # 반복 후 더이상 예산을 지원해줄 수 없다면
            break # 뒤도 안돌아보고 break!
    return answer

if __name__ == "__main__":
    print(solution([1, 3, 2, 5, 4], 9))
    print(solution([2, 2, 3, 3], 10))