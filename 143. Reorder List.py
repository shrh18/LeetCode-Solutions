# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return head
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow = head, head

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

        fast = slow.next
        slow.next = None

        prev, curr, ahead = fast, fast, fast.next
        while ahead is not None:
            fast.next = None
            prev = curr
            curr = ahead
            ahead = ahead.next
            curr.next = prev

        cur1, cur2 = head, curr


        while cur1 is not None and cur2 is not None:
            a1 = cur1.next
            cur1.next = cur2
            cur1 = a1

            a2 = cur2.next
            cur2.next = cur1
            cur2 = a2