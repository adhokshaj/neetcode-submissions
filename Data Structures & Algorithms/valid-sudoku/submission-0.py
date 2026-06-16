class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r, c = len(board), len(board[0])

        def validate_row(board):
            for row in range(r):
                seen = set()
                for col in range(c):
                    if board[row][col] == '.':
                        continue
                    if (int(board[row][col]) in seen or 
                    int(board[row][col]) > 9 or 
                    int(board[row][col]) < 1):
                        return False
                    seen.add(int(board[row][col]))
            return True

        def validate_col(board):
            for col in range(c):
                seen = set()
                for row in range(r):
                    if board[row][col] == '.':
                        continue
                    if (int(board[row][col]) in seen or 
                    int(board[row][col]) > 9 or 
                    int(board[row][col]) < 1):
                        return False
                    seen.add(int(board[row][col]))
            return True

        def validate_square(board):
            seen = [[set() for _ in range(r)] for _ in range(c)]
            for row in range(r):
                for col in range(c):
                    if board[row][col] == '.':
                        continue
                    # print(board[row][col], seen[row//3][col//3], row//3, col//3, row, col)
                    if (int(board[row][col]) in seen[row//3][col//3] or 
                    int(board[row][col]) > 9 or 
                    int(board[row][col]) < 1):
                        # print("Here", board[row][col], seen[row//3][col//3], row//3, col//3, row, col)
                        return False
                    seen[row//3][col//3].add(int(board[row][col]))
            return True

        return (validate_row(board) and 
                validate_col(board) and
                validate_square(board))

        

                


        