class Solution:
    def __init__(self) -> None:
        self.visited = []

    def exist(self, board: list, word: str) -> bool:
        m = len(board)
        n = len(board[0])

        starting_char = word[0]
        starting_point = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == starting_char:
                    starting_point.append((i, j))
        
        self.visited = [ [False] * n for i in range(m) ]
        idx = 0
        for i, j in starting_point:
            if self.search(board, word, i, j, idx):
                return True
        return False
    
    def search(self, board: list, word: str, i: int, j: int, idx: int) -> bool:
        if idx == len(word):
            return True
        
        m = len(board)
        n = len(board[0])

        if i < 0 or m <= i or j < 0 or n <= j:
            return False
        if self.visited[i][j] == True:
            return False
        print(f'current char : {board[i][j]}, need to {word[idx]}')
        if board[i][j] != word[idx]:
            return False
        
        self.visited[i][j] = True

        result = self.search(board, word, i, j + 1, idx + 1) or self.search(board, word, i + 1, j, idx + 1) or self.search(board, word, i, j - 1, idx + 1) or self.search(board, word, i - 1, j, idx + 1)
        if not result:
            self.visited[i][j] = False
        
        return result


solution = Solution()
sol_result = solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
print(f'case 1 is True, result is {sol_result}')

sol_result = solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
print(f'case 2 is True, result is {sol_result}')

sol_result = solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
print(f'case 3 is False, result is {sol_result}')

sol_result = solution.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")
print(f'case 4 is False result is {sol_result}')