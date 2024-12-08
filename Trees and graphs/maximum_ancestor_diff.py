# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Find the maximum value v for which there exist different nodes a and b
        where v = |a.val - b.val| and a is an ancestor of b.
        
        :param root: TreeNode, root of the binary tree
        :return: int, maximum difference between ancestor and descendant node values
        """
        def helper(node, current_min, current_max):
            if not node:
                return current_max - current_min
            
            # Update the current minimum and maximum values
            current_min = min(current_min, node.val)
            current_max = max(current_max, node. val)
            
            # Recurse for left and right substrees
            left_diff = helper(node.left, current_min, current_max)
            right_diff = helper(node.right, current_min, current_max)
            
            # Return the maximum difference found
            return max(left_diff, right_diff)
        
        # Start the recursion with the root's value as both the initial min and max.
        return helper(root, root.val, root.val)
        
# Complexity Analysis
# Time Complexity: O(N) 
#   - Each node in the tree is visited exactly once.
# Space Complexity: O(H)
#   - H is the height of the tree. In the worst case (skewed tree), H = N.
#   - In the best case (balanced tree), H = Log(N).
        
