def solution(answers: list):
    # 수포자 1, 2, 3번의 정답 리스트 만들기
    no1 = [1, 2, 3, 4, 5] * 2000
    no2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    no3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    # 제공된 정답지에 맞춰 슬라이싱
    no1 = no1[:len(answers)]
    no2 = no2[:len(answers)]
    no3 = no3[:len(answers)]

    # 정답수 count
    supoja = {1: 0, 2: 0, 3: 0}
    for an, n1, n2, n3 in zip(answers, no1, no2, no3):
        if an == n1:
            supoja[1] += 1
        if an == n2:
            supoja[2] += 1
        if an == n3:
            supoja[3] += 1
    
    # value가 최댓값인 수포자들을 가지고 리스트 컴프리헨션
    answer = [k for k, v in supoja.items() if max(supoja.values()) == v]
    return answer

if __name__ == "__main__":
    example1 = [1, 2, 3, 4, 5]
    print(solution(example1))
    example2 = [1, 3, 2, 4, 2]
    print(solution(example2))