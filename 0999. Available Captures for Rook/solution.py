class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ret = 0
        for l in range(8):
            for r in range(8):
                if board[l][r] == "R":
                    ret += self.search(board, r, l, 1, 0) 
                    ret += self.search(board, r, l, -1, 0) 
                    ret += self.search(board, r, l, 0, 1)
                    ret += self.search(board, r, l, 0, -1)
                    return ret
    def search(self, board, posX, posY, moveX, moveY):
        if 0 > posX or posX >= 8 or 0 > posY or posY >= 8 or "B" == board[posY][posX]:
            return 0
        elif "p" == board[posY][posX]:
            return 1
        return self.search(board, posX + moveX, posY + moveY, moveX, moveY)
