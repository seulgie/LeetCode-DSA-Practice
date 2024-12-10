class TreeNode:
    """Class to represent a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    """
    Finds the length of the longest path from the root to a leaf.

    Args:
        root (TreeNode): The root of the binary tree.

    Returns:
        int: The length of the longest path from the root to a leaf.

    Complexity:
        Time Complexity:
            - The function visits every node in the binary tree exactly once.
            - For each node, it computes the maximum depth of the left and right subtrees.
            - Therefore, the time complexity is O(n), where n is the total number of nodes.
        
        Space Complexity:
            - The function uses recursion, and the maximum depth of recursion corresponds to the height of the tree.
            - For a balanced binary tree, the height is O(log n), resulting in O(log n) space complexity.
            - For an unbalanced tree, the height can be O(n), resulting in O(n) space complexity.
    """
    if root is None:
        return 0

    left_depth = longest_path_length(root.left)
    right_depth = longest_path_length(root.right)

    return max(left_depth, right_depth) + 1

