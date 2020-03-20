class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        i, n = start, len(distance)
        clockwise, counterclockwise, carry = 0, 0, False
        while True:
            if destination == i:
                carry = True
            if i == start and carry:
                break
            if not carry:
                clockwise += distance[i]
            if carry:
                counterclockwise += distance[i]
            i = (i+1)%n
            
        return min(clockwise, counterclockwise)
