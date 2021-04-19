def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    return answer/len(arr)

if __name__ == "__main__":
    print(solution([1,2,3,4]))
    print(solution([5,5]))