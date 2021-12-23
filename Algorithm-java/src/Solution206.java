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
class Solution206 {
    public ListNode reverseList(ListNode head) {

        ListNode answer = new ListNode();
        ListNode current = answer.next;

        while (head != null){
            ListNode next = head.next;
            head.next = current;
            current = head;
            head = next;
        }


        return current;

    }
}