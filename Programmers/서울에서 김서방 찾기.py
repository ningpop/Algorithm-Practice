def solution(seoul):
    result = 0
    for index, value in enumerate(seoul):
        if value == 'Kim':
            result = index
    answer = f'김서방은 {result}에 있다'
    return answer