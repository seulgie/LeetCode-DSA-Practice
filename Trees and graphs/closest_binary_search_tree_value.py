# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        Find the value in the BST closest to the target.
        If there are multiple values equally close, return the smallest one.
        
        Time Complexity:
          - O(h): In the worst case, we traverse the height of the tree.
          For a balanced tree, h = O(log n). For a skewed tree, h = O(n).
          
        Space Complexity:
          - O(1): No extra space is used apart from variables.
          
        :param root: Root node of the BST
        :param target: The target value
        :return: The value closest to the target
        """
        closest = root.val # Initialize closest value with the root's value
        
        while root:
            # Update closest if the current node's value is closer to the target
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            elif abs(root.val - target) == abs(closest - target) and root.val < closest:
                closest = root.val
                
            # Move left or right based on the target value
            if target < root.val:
                root = root.left
            else:
                root = root.right
                
        return closest
    
