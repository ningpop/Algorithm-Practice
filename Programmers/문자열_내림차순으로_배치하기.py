def solution(s: str) -> str:
    return ''.join(sorted(s, reverse=True))

if __name__ == "__main__":
    print(solution("Zbcdefg"))