# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        print(arr)
        l = len(arr)
        if l>1:
            newNode = ListNode(arr[0])
            newhead = newNode
            for i in range(1, len(arr)):
                newhead.next = ListNode(arr[i])
                newhead = newhead.next
            return newNode
        elif l==1:
            return head
        else:
            return None
