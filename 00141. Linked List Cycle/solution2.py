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
        d = {}
        while head:
            h = head
            if h in d:
                return True
            d[h] = 1
            head = head.next
        return False
