class Solution:
    def reorganizeString(self, s: str) -> str:
        alpha_dict = {}
        for c in s:
            if alpha_dict.get(c) == None:
                alpha_dict[c] = 0
            alpha_dict[c] += 1

        import heapq
        hq = []
        for k, v in alpha_dict.items():
            heapq.heappush(hq, (-v, k))

        result = ''
        while hq:
            first_char = heapq.heappop(hq)

            if not hq:
                if -first_char[0] > 1:
                    return ''
                result += first_char[1]
                break
            second_char = heapq.heappop(hq)

            result += first_char[1]
            result += second_char[1]

            if -first_char[0] > 1:
                heapq.heappush(hq, (first_char[0] + 1, first_char[1]))

                if -second_char[0] > 1:
                    heapq.heappush(hq, (second_char[0] + 1, second_char[1]))

        return result


solution = Solution()
answer = solution.reorganizeString("aab")
print(f'{answer=}')

answer = solution.reorganizeString("aaab")
print(f'{answer=}')
