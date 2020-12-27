# Merge two sorted linked lists and return it as a new sorted list.
# The new list should be made by splicing together the nodes of the first two lists.

from heapq import *

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        min_heap = []
        heappush(min_heap, (l1.val, l1))
        heappush(min_heap, (l2.val, l2))
        result_head = result_tail = None
        while min_heap:
            node = heappop(min_heap)
            if not result_head:
                result_head = result_tail = node[1]
            else:
                result_tail.next = node[1]
                result_tail = result_tail.next
            if node[1].next:
                heappush(min_heap, (node[1].next.val, node[1].next))
        return result_head

if __name__ == '__main__':
    list1 = Solution().ListNode(1)
    list1.next = Solution().ListNode(2)
    list1.next.next = Solution().ListNode(4)
    list2 = Solution().ListNode(1)
    list2.next = Solution().ListNode(3)
    list2.next.next = Solution().ListNode(4)
    mergeTwoLists_1 = Solution().mergeTwoLists(list1, list2)