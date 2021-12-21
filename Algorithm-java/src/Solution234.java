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
public class Solution234 {
    public boolean isPalindrome(ListNode head) {

        Deque<Integer> stack = new ArrayDeque<Integer>();

        while (head != null) {
            stack.addLast(head.val);
            head = head.next;
        }

        while (stack.size() > 1) {
            if (stack.removeFirst() != stack.removeLast()) {
                return false;
            }
        }
        return true;
    }
}

