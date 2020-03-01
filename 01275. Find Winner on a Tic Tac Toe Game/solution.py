class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        i = 1
        grid = [" "] * 9
        checks = [[0, 1, 2], [3, 4, 5], [6, 7, 8], \
                  [0, 3, 6], [1, 4, 7], [2, 5, 8], \
                  [0, 4, 8], [2, 4, 6]]
            
        for (r, c) in moves:
            grid[(r*3)+c] = "B" if i % 2 == 0 else "A"
            i+=1
        
        for arr in checks:
            first = grid[arr[0]]
            for c in arr:
                if first != grid[c] or grid[c] == " ":
                    first = ""
                    break
            if first != "":
                return first
            
        return "Draw" if len(moves) == 9 else "Pending"
