class RecentCounter(object):

    def __init__(self):
        self.arr = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.arr.append(t)
        while self.arr[-1] - self.arr[0] > 3000:
            self.arr.pop(0)
        return len(self.arr)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
