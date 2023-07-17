class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = True
        for i in range(9):
            if not self.is_solvable(board, 'row', i, 0, i, 9):
                result = False
                break
            if not self.is_solvable(board, 'col', 0, i, 9, i):
                result = False
                break

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                if not self.is_solvable(board, 'sub_box', i, j, i + 3, j + 3):
                    result = False
                    break
        
        return result

    def is_solvable(self, board, direction, a1, a2, b1, b2):
        static_list = [ str(n) for n in range(1, 10) ]
        print(f'static_list = {static_list}')

        if direction == 'row':
            for i in range(9):
                num = board[a1][i]
                print(f'({a1}, {i}) = {num}')
                if num != '.':
                    print(f'static_list = {static_list}')
                    if num in static_list:
                        print(f'here?')
                        static_list.remove(num)
                    else:
                        return False
        elif direction == 'col':
            for i in range(9):
                num = board[i][a2]
                if num != '.':
                    if num in static_list:
                        static_list.remove(num)
                    else:
                        return False
        elif direction == 'sub_box':
            for i in range(a1, b1):
                for j in range(a2, b2):
                    num = board[i][j]
                    if num != '.':
                        if num in static_list:
                            static_list.remove(num)
                        else:
                            return False
        return True