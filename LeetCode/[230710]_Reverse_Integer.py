class Solution:
    def reverse(self, x: int) -> int:
        result = ''
        
        if x < 0:
            result += '-'
            x = -x
        
        while x >= 10:
            quotient = x // 10
            remainder = x % 10
            if result != '' or result != '-':
                result += str(remainder)
            x = quotient

        result += str(x)
        answer = int(result)
        
        if answer > 2147483647 or answer < -2147483648:
            return 0

        return answer