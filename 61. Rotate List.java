/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        int size = 0;
        ListNode gg = head;
        while(gg!=null){
            size++;
            gg = gg.next;
        }
        System.out.println("Size of list - " + size);
        if(k>0 && k>=size && size!=0){
            k = k%size;
        }
        if(head != null && head.next == null){
            return head;
        }
        else if(head != null && head.next.next != null){
            ListNode rr = new ListNode();
            for(int i=0; i<k; i++){
                ListNode curr = head;
                while(curr.next.next != null){
                    curr = curr.next;
                }
                ListNode sl = curr;
                ListNode l = curr.next;
                sl.next = null;
                l.next = head;
                head = l;
            }
            return head;
        }
        else if(head !=null && head.next != null){
            if(k%2 == 0){
                return head;
            }else{
                ListNode kk = head.next;
                head.next.next = head;
                head.next = null;
                return kk;
            }
        }
        else{
            return null;
        }
    }
}