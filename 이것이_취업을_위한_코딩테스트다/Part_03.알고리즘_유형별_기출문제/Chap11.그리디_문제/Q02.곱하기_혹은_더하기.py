S = input()

s_list = [int(i) for i in S] # 문자열 S를 정수 리스트로 변환

stack = []
stack.append(s_list[0]) # 스택에 가장 첫번째 숫자를 삽입
for i in s_list[1:]: # 두번째 숫자부터 반복
    # if stack[-1] == 0 or i == 0: # 기존 풀이
    if stack[-1] <= 1 or i <= 1: # 첫번째 숫자가 0 or 1이거나 다음에 올 숫자가 0 or 1이라면
        stack.append('+') # 가장 큰 수를 위해 + 삽입
    else:
        stack.append('*') # 그 외의 경우 가장 큰 수를 위해 * 삽입
    
    stack.append(i) # 그 다음 수 삽입

    cal = '' # 계산식 문자열 초기화
    for j in stack:
        cal += str(j) # 스택에 있는 내용들 꺼내서 계산식 문자열 만들기
    result = eval(cal) # 각 과정마다 계산 결과를 저장

    stack.clear() # 스택 비우고
    stack.append(result) # 계산한 값 스택에 삽입

print(result)