# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        i=0
        while i<len(lists):
            if not lists[i]:
                del lists[i]
            else:
                i+=1

        while len(lists)>1:
            l1 = lists[0]
            l2 = lists[1]
            del lists[0]
            del lists[0]
            cur1 = l1
            cur2 = l2
            res = []
            while cur1!=None and cur2!=None:
                if cur1.val<cur2.val:
                    res.append(cur1.val)
                    cur1 = cur1.next
                elif cur2.val<cur1.val:
                    res.append(cur2.val)
                    cur2 = cur2.next
                else:
                    res.append(cur1.val)
                    cur1 = cur1.next
                    res.append(cur2.val)
                    cur2 = cur2.next
            
            while cur1!=None:
                res.append(cur1.val)
                cur1 = cur1.next
            while cur2!=None:
                res.append(cur2.val)
                cur2 = cur2.next

            newNode = ListNode(res[0])
            newCur = newNode
            for i in range(1,len(res)):
                newCur.next = ListNode(res[i])
                newCur = newCur.next
            lists.append(newNode)

        if lists:
            return lists[0]
        else:
            return None

            
        

