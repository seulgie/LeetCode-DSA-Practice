# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Finds the minimum depth of a binary tree.
        
        Args:
        root (TreeNode): The root of the binary tree.
        
        Returns:
        int: The minimum depth of the tree.
        """
        if not root:
            return 0
        
        # Use a queue to perform Breath-First Search (BFS)
        queue = deque([(root, 1)]) # (node, current depth)
        
        while queue:
            node, depth = queue.popleft()
            
            # If the current node is a leaf, return its depth
            if not node.left and not node. right:
                return depth
            
            # Add children to the queue with incremented depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
                
# Complexity Analysis:
# Time Complexity: O(n), where n is the number of nodes in the tree.
#      Each node is visited once in the BFS traversal.
# Space Complexity: O(d), where d is the maximum depth of the tree.
        
