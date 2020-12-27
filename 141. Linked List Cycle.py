# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where the tail connects to.
# If pos == -1, then there is no cycle in the linked list.

# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == '__main__':
    list_node21 = Node(3)
    list_node22 = Node(2)
    list_node23 = Node(0)
    list_node24 = Node(-4)
    list_node21.next = list_node22
    list_node22.next = list_node23
    list_node23.next = list_node24
    list_node24.next = list_node22
    print(Solution().hasCycle(list_node21))
    list_node25 = Node(1)
    print(Solution().hasCycle(list_node25))