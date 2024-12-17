class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    """
    Determines if there exists a path from root to a leaf where the sum of nodes equals targetSum.

    Args:
        root (TreeNode): The root of the binary tree.
        targetSum (int): The target sum to find in the root-to-leaf path.

    Returns:
        bool: True if such a path exists, False otherwise.
    """
    def dfs(node, curr):
        if not node:
            return False
        
        # if both children are null, then the node is a leaf
        if node.left == None and node.right == None:
            return (curr + node.val) == targetSum
        
        curr += node.val
        left = dfs(node.left, curr)
        right = dfs(node.right, curr)
        return left or right
    
    return dfs(root, 0)

# Complexity Analysis:
# Time Complexity: O(N) where N is the number of nodes in the binary tree.
#   - Each node is visited once, hence the time complexity is linear.
# Space Complexity: O(H) where H is the height of the binary tree.
#   - In the worst case (skewed tree), H = N leading to O(N) space.
#   - In the best case (balanced tree), H = log(N), leading to O(log N) space.
