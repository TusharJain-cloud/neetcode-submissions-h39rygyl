# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursion
        if head is None or head.next is None:
            return head
        
        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head
        # prev, current = None, head
        
        # while current:
        #     third = current.next
        #     current.next = prev
        #     prev = current
        #     current = third
        
        # return prev


        