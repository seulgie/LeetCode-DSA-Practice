# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        # Traverse the Linked List
        while current and current.next:
            # If current value is the same as next value, skip the next node
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # Otherwise, move to the next node
                current = current.next
                
        return head
        
