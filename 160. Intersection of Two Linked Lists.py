# Write a program to find the node at which the intersection of two singly linked lists begins.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa is not None else headB
            pb = pb.next if pb is not None else headA

        return pa if pa else None

if __name__ == '__main__':
    list_node6 = ListNode(4)
    list_node7 = ListNode(1)
    list_node8 = ListNode(8)
    list_node9 = ListNode(4)
    list_node10 = ListNode(5)
    list_node11 = ListNode(5)
    list_node12 = ListNode(0)
    list_node13 = ListNode(1)
    list_node14 = ListNode(8)
    list_node15 = ListNode(4)
    list_node16 = ListNode(5)
    list_node6.next = list_node7
    list_node7.next = list_node8
    list_node8.next = list_node9
    list_node9.next = list_node10
    list_node11.next = list_node12
    list_node12.next = list_node13
    list_node13.next = list_node14
    list_node14.next = list_node15
    list_node15.next = list_node16
    print(Solution().getIntersectionNode(list_node6, list_node11))