def solution(s: str) -> bool:
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
            return True
        except:
            return False
    return False

if __name__ == "__main__":
    print(solution("a234"))
    print(solution("1234"))