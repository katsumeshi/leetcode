# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return self.checkCycle(head, [])
    
    def checkCycle(self, head, arr):
        if head is None:
            return False
        address = hex(id(head))
        if address in arr:
            return True
        arr.append(address)
        
        return self.checkCycle(head.next, arr)
