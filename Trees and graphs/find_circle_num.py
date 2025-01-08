from collections import defaultdict
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        seen = set()
        ans = 0
        
        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)
        
        return ans

# Example Usage
isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
solution = Solution()
print(solution.findCircleNum(isConnected))  # Output: 2

"""
Complexity Analysis:

1. Time Complexity:
   - Graph Construction: The nested loop iterates over the upper triangular part of the matrix (excluding the diagonal), taking O(n^2 / 2), which simplifies to O(n^2).
   - DFS Traversal: In the worst case, each city and its connections are visited once. The total number of edges in the graph is at most O(n^2), so the DFS traversal is O(n^2) in the worst case.
   - Overall Time Complexity: O(n^2).

2. Space Complexity:
   - Graph Representation: The adjacency list (dictionary of lists) takes O(n^2) space in the worst case when all cities are interconnected.
   - Visited Set: The `seen` set takes O(n) space to store all visited cities.
   - Recursive Stack: The DFS recursive stack can grow up to O(n) in the worst case.
   - Overall Space Complexity: O(n^2).
"""
