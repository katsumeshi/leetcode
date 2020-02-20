class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        arr=[]
        for o in ops:
            if o == "+":
                arr.append(arr[len(arr)-1]+arr[len(arr)-2])
            elif o == "D":
                arr.append(arr[len(arr)-1]*2)
            elif o == "C":
                del arr[len(arr)-1]
            else:
                arr.append(int(o))
        return sum(arr)
