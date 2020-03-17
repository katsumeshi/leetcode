# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        i = 0
        while head is not None:
            arr.append(head)
            head = head.next
            i+=1
        return arr[len(arr)/2]
