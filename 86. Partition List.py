# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or head.next is None:
            return head

        lessHead, moreHead = None, None
        lc, hc = lessHead, moreHead
        curr = head
        while curr is not None:
            if curr.val < x:
                if lessHead == None:
                    lessHead = ListNode(curr.val)
                    lc = lessHead  
                else:
                    lc.next = ListNode(curr.val)
                    lc = lc.next
            else:
                if moreHead == None:
                    moreHead = ListNode(curr.val)
                    hc = moreHead
                else:
                    hc.next = ListNode(curr.val)
                    hc = hc.next

            curr = curr.next
            
        if lessHead is None or moreHead is None:
            return head

        lc.next = moreHead
        return lessHead
                    

