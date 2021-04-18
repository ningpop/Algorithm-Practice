def solution(arr):
    answer = []
    for idx, value in enumerate(arr):
        if idx == 0:
            answer.append(value)
            continue
        if value == arr[idx-1]:
            continue
        answer.append(value)
    return answer

if __name__ == "__main__":
    print(solution([1,1,3,3,0,1,1]))
    print(solution([4,4,4,3,3]))