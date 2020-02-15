class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        pos = [0, 0]
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        index = 1
        oSets = set(map(tuple, obstacles))
            
        maxSquare = 0
        for c in commands:
            if c < 0:
                index += 1 if c == -2 else -1
                index = index % len(direction)
                continue
                
            for i in range(c):
                nextPos = [pos[0] + direction[index][0], pos[1] + direction[index][1]]
                if (nextPos[0], nextPos[1]) in oSets:
                    break
                pos = nextPos
            maxSquare = max(maxSquare, pos[0]**2+pos[1]**2)
        return maxSquare
