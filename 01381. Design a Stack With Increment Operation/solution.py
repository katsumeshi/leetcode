class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize = maxSize
        self.arr = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.maxSize > len(self.arr):
            self.arr.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.arr) > 0:
            return self.arr.pop()
        return -1
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(min(k, len(self.arr))):
            self.arr[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
