# Binary Search Tree Sum of Range
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def range_sum_bst(root, low, high):
    if not root:
        return 0

    # If the current node's value is within the range, include it in the sum.
    if low <= root.val <= high:
        return root.val + range_sum_bst(root.left, low, high) + range_sum_bst(root.right, low, high)

    # If the current node's value is less than `low`, skip the left subtree.
    elif root.val < low:
        return range_sum_bst(root.right, low, high)

    # If the current node's value is greater than `high`, skip the right subtree.
    else:
        return range_sum_bst(root.left, low, high)

# Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes in the tree. In the worst case, we visit all nodes.
# Space Complexity: O(H), where H is the height of the tree. This is the space used by the recursion stack.
