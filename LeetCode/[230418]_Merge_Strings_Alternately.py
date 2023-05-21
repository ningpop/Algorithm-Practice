class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_list = list(word1)
        word1_list.reverse()
        word2_list = list(word2)
        word2_list.reverse()

        result = ''
        while word1_list or word2_list:
            c1 = word1_list.pop() if word1_list else False
            c2 = word2_list.pop() if word2_list else False
            if c1:
                result += c1
            if c2:
                result += c2

        return result