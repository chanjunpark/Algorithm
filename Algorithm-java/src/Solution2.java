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
class Solution2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode answer = new ListNode(0);
        ListNode current = answer;

        while(l1 != null && l2!= null){
            int sum = l1.val + l2.val;
            if(current.val>=10){
                current.val = current.val%10;
                sum += 1;
            }
            ListNode newNode = new ListNode(sum);
            current.next = newNode;
            current = current.next;
            l1 = l1.next;
            l2 = l2.next;
        }

        while(l1 != null){
            if(current.val>=10){
                current.val = current.val%10;
                l1.val += 1;
            }
            ListNode newNode = new ListNode(l1.val);
            current.next = newNode;
            current = current.next;
            l1 = l1.next;

        }

        while(l2 != null){
            if(current.val>=10){
                current.val = current.val%10;
                l2.val += 1;
            }
            ListNode newNode = new ListNode(l2.val);
            current.next = newNode;
            current = current.next;
            l2 = l2.next;
        }

        if(current.val>=10){
            current.val = current.val%10;
            ListNode newNode = new ListNode(1);
            current.next = newNode;
            current = current.next;
        }

        return answer.next;


    }
}