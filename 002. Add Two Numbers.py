class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = 0
        dummy = head = ListNode(0)
        while l1 or l2 or result > 0:
            if l1:
                result += l1.val
                l1 = l1.next
            if l2:
                result += l2.val
                l2 = l2.next
            head.next = ListNode(result % 10)
            result //= 10
            head = head.next
        return dummy.next