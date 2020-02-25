# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        h = head
        prev = head
        while h.next:
            prev.next = h.next
            if h.val == val:
                prev.next = h.next.next
            h = h.next
