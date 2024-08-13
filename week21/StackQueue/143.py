# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return
        elif head.next and not head.next.next:
            return

        original_head = head
        reversed_head = ListNode()

        len_head = 0
        while original_head:
            reversed_head = ListNode(original_head.val, reversed_head)
            original_head = original_head.next
            len_head += 1

        n = 1
        while head.next and reversed_head.next:
            head.next = ListNode(reversed_head.val, head.next)

            n += 2

            if n == len_head:
                head.next.next.next = None
                return
            elif n == len_head + 1:
                head.next.next = None
                return

            head = head.next.next
            reversed_head = reversed_head.next



