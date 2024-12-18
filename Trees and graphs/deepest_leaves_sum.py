from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepestLeavesSum(root):
    """
    Returns the sum of the values of the deepest leaves in the binary tree.

    Args:
        root (TreeNode): The root of the binary tree.

    Returns:
        int: Sum of the values of the deepest leaves.
    """
    if not root:
        return 0

    # Initialize a queue for BFS
    queue = deque([root])
    deepest_sum = 0

    while queue:
        level_size = len(queue)  # Number of nodes at the current level
        current_level_sum = 0   # Sum of nodes at the current level

        for _ in range(level_size):
            node = queue.popleft()
            current_level_sum += node.val

            # Add child nodes to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Update the deepest sum after processing the current level
        deepest_sum = current_level_sum

    return deepest_sum

# Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes in the binary tree. Each node is visited once.
# Space Complexity: O(W), where W is the maximum width of the tree (the maximum number of nodes at any level).
