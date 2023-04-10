class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)
            else:
                if not stack:
                    return False
                poped_bracket = stack.pop()
                if not self.isSameType(poped_bracket, bracket):
                    return False
        if stack:
            return False
        return True
    
    def isSameType(self, s1: str, s2: str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}
        if brackets[s1] == s2:
            return True
        return False