# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        merge_list = ListNode()
        merge = merge_list

        while True:
            try:
                post = min([linked_list.val for idx, linked_list in enumerate(lists) if linked_list != None])
            except ValueError as v:
                break
            for idx in range(len(lists)):
                if lists[idx] != None and lists[idx].val == post:
                    temp = lists[idx].next
                    lists[idx].next = None
                    merge.next = lists[idx]
                    lists[idx] = temp
                    merge = merge.next

        return merge_list.next