# Given a singly linked list, determine if it is a palindrome.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        # slow.next = None

        head2 = self.isPalindromeLinkedList_ReverseList(head2)

        while head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return True

    def isPalindromeLinkedList_ReverseList(self, head):
        if not head or not head.next:
            return head
        previous = None
        while head:
            temp = head.next
            head.next = previous
            previous = head
            head = temp
        return previous