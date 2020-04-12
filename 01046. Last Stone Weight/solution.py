class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones) == 0:
            return 0
        elif len(stones) == 1:
            return stones.pop()
        stones = sorted(stones)
        a = stones.pop()
        b = stones.pop()
        if a != b:
            stones.append(a - b)
        return self.lastStoneWeight(stones)
