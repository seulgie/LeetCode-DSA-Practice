# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Computes the diameter of a binary tree.
        
        Args:
           root (TreeNode): The root of the binary tree.
           
        Returns:
           int: The length of the diameter of the tree (number of edges).
           
        Time Complexity:
           - Each node in the tree is visited exactly once.
           - At each node, a constant amount of work is done to calculate.
           - Therefore, the time complexity is O(n), where n is the number of nodes.
           
        Space Complexity:
           - The function uses recursion, and the maximum depth of recursion corresponds to the height of the tree.
           - For a balanced binary tree, the height is O(long n), so the space complexity is O(long n).
           - For a completely unbalanced tree, the height is O(n), so the space complexity is O(n).
        """
        diameter = 0
        
        def depth(node):
            nonlocal diameter
            if not node:
                return 0
            
            # Recursively find the depth of left and right subtrees
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # Update the diameter with the longest path through the current node
            diameter = max(diameter, left_depth + right_depth)
            
            # Return the height of the current node
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return diameter
        
