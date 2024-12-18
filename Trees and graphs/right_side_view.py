from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    """
    Returns the values of the nodes visible from the right side of the binary tree.

    Args:
        root (TreeNode): The root of the binary tree.

    Returns:
        List[int]: The list of node values visible from the right side.
    """
    if not root:
        return []

    # Result list to store the rightmost nodes at each level
    result = []

    # Use a queue to perform BFS
    queue = deque([root])

    while queue:
        level_size = len(queue)
        
        # Iterate through the current level
        for i in range(level_size):
            node = queue.popleft()

            # If it's the last node in this level, add to result
            if i == level_size - 1:
                result.append(node.val)
            
            # Add children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result

# Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes in the tree. Each node is visited once.
# Space Complexity: O(W), where W is the maximum width of the tree (the maximum number of nodes at any level).
