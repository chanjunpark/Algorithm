# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = None
        add = 0

        while True:
            if head == None:
                if l1.val + l2.val + add >= 10:
                    head = ListNode((l1.val + l2.val + add) % 10)
                    add = (l1.val + l2.val + add) // 10
                else:
                    head = ListNode(l1.val + l2.val + add)
            else:
                current = head
                while current.next != None:
                    current = current.next
                if l1.val + l2.val + add >= 10:
                    current.next = ListNode((l1.val + l2.val + add) % 10)
                    add = (l1.val + l2.val + add) // 10
                else:
                    current.next = ListNode(l1.val + l2.val + add)
                    add = 0
            if l1.next == None and l2.next == None:
                if add != 0:
                    current = head
                    while current.next != None:
                        current = current.next
                    current.next = ListNode(add)
                break
            elif l1.next == None and l2.next != None:
                l1 = ListNode()
                l2 = l2.next
            elif l1.next != None and l2.next == None:
                l1 = l1.next
                l2 = ListNode()
            else:
                l1 = l1.next
                l2 = l2.next

        return head
