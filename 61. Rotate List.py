# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head != None:
            if k==0:
                return head
            length = 1
            curr = head
            last = None
            while curr.next != None:
                length = length +1 
                curr = curr.next
                if curr.next == None:
                    last = curr
            print(length)

            if length == 1:
                return head
            
            k = k%length
            if k==0:
                return head
            newHead = None
            newCurr = head
            for i in range(1, length-k):
                newCurr = newCurr.next
                i = i+1
            print("newCurr - ", newCurr.val)
            newHead = newCurr.next
            last.next = head
            newCurr.next = None

            return newHead
        else:
            return head
        