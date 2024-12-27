# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Insert a value into the Binary Search Tree (BST).

        Time Complexity:
        - Worst-case: O(h), where h is the height of the tree. In the worst case, 
          this occurs when the tree is skewed (like a linked list).
        - Best-case: O(log n), when the tree is balanced.

        Space Complexity:
        - Worst-case: O(h), where h is the height of the tree, due to recursion stack.
        - Best-case: O(log n), when the tree is balanced.
        """

        # If the root is None, create a new node with the given value and return it
        if not root:
            return TreeNode(val)

        # Otherwise, find the correct place for the new value
        if val < root.val:
            # Go to the left subtree
            root.left = self.insertIntoBST(root.left, val)
        else:
            # Go to the right subtree
            root.right = self.insertIntoBST(root.right, val)

        # Return the root of the modified BST
        return root
