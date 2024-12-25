# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # Step 1: Create a dummy node and set up pointers
        # The dummy node simplifies edge caes, such as reversing from the head.
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Step 2: Move 'prev' to the node just before the 'left' position.
        for _ in range(left - 1):
            prev = prev.next
            
        # 'start' points to the first node of the sublist to reverse.
        start = prev.next
        # 'then' points to the node that will be reversed.
        then = start.next
        
        # Step 3: Reverse the sublist from 'left' to 'right'.
        # Repeat the process 'right - left' times.
        for _ in range(right - left):
            # Step 3.1: Disconnect 'then' from the rest of the list and reconnect it at 'prev.next'.
            start.next = then.next
            then.next = prev.next
            prev.next = then
            # Step 3.3: Move 'then' to the next node to be processed.
            then = start.next
            
        # Step 4: Return the modified list, starting from the dummy's next node.
        return dummy.next
    
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as the algorithm reverses the list in place without using extra space for data structures.

