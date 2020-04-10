class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.arr.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.arr) > 0:
            self.arr.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.arr) > 0:
            return self.arr[len(self.arr)-1]
        return 0
        

    def getMin(self):
        """
        :rtype: int
        """
        m = sys.maxint
        for n in self.arr:
            m = min(n, m)
        return m
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
