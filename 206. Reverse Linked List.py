# Reverse a singly linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head

        previous = None
        while head:
            temp = head.next
            head.next = previous
            previous = head
            head = temp
        return previous