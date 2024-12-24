from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform a zigzag level order traversal of a binary tree.
        :param root: TreeNode
        :return: List[List[int]]
        """
        if not root:
            return []
        
        results = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            level = deque()
            
            for _ in range(level_size):
                node = queue.popleft()
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            results.append(list(level))
            left_to_right = not left_to_right
            
        return results
    
# Time Complexity: O(N), where N is the total number of nodes in the tree
# Space Complexity: O(N) for the queue to hold nodes at each level
        
