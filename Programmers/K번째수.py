def solution(array, commands):
    answer = []
    for a in commands:
        start = a[0]
        end = a[1]
        th = a[2]
        cut_array = array[start-1:end]
        cut_array.sort()
        answer.append(cut_array[th-1])
    return answer