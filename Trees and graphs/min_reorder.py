from collections import defaultdict
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        Problem:
        Given n cities and n-1 roads represented as directed edges, determine the minimum number of roads that need to be reversed so that every city can reach city 0.

        Approach:
        - Build an undirected graph and track directed roads in a set.
        - Use DFS starting from city 0 to count the necessary reversals.

        Complexity Analysis:
        - Time Complexity: O(n), where n is the number of cities (each node and edge is visited once).
        - Space Complexity: O(n), for the graph representation and recursion stack.
        """
        roads = set()  # To track directed roads
        graph = defaultdict(list)  # Undirected graph representation
        
        # Build the graph and store directed roads
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x, y))
        
        def dfs(node):
            ans = 0
            for neighbor in graph[node]:
                if neighbor not in seen:  # Visit unvisited neighbors
                    if (node, neighbor) in roads:  # Road needs to be reversed
                        ans += 1
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            return ans
        
        seen = {0}  # Start DFS from city 0
        return dfs(0)

# Example Usage
n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
solution = Solution()
print(solution.minReorder(n, connections))  # Output: 3
