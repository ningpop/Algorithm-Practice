class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        s1 = ''.join(sorted(s1))
        for i in range(0, len2 - len1 + 1):
            if s1 == ''.join(sorted(s2[i : i + len1])):
                return True
        return False


solution = Solution()
result = solution.checkInclusion("ab", "eidbaooo")
print(f'case 1 is True, result 1 is {result}\n')

result = solution.checkInclusion("ab", "eidboaoo")
print(f'case 2 is False, result 2 is {result}\n')

result = solution.checkInclusion("dinitrophenylhydrazine", "acetylphenylhydrazine")
print(f'case 3 is False, result 3 is {result}\n')

result = solution.checkInclusion("adc", "dcda")
print(f'case 4 is True, result 3 is {result}\n')