class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            hashset = set()
            for col in range(len(board[row])):
                if board[row][col] != '.' and board[row][col] in hashset:
                    return False
                hashset.add(board[row][col])


        for col in range(len(board[0])):
            hashset = set()
            for row in range(len(board)):
                if board[row][col] != '.' and board[row][col] in hashset:
                    return False
                hashset.add(board[row][col])

        boxes = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    box_index = (row // 3) * 3 + (col // 3)
                    if board[row][col] in boxes[box_index]:
                        return False
                    boxes[box_index].add(board[row][col])

        return True
