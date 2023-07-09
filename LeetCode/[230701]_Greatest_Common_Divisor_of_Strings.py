import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_length = len(str1)
        str2_length = len(str2)

        num = math.gcd(str1_length, str2_length)
        word = str1[:num]

        if word != str2[:num]:
            return ''
        for i in range(0, len(str1), num):
            if str1[i:i+num] != word:
                return ''

        for i in range(0, len(str2), num):
            if str2[i:i+num] != word:
                return ''

        return str1[:num]