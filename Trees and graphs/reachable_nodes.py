class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        """Convert restricted nodes into a set for O(1) Lookup
        
        Time Complexity: O(n)
          - We traverse each edge once using DFS, leading to O(n) complexity.
          - Since we use a set for visited nodes and restricted nodes, lookup operations are O(1).
          
        Space Complexity: O(n)
          -The adjacency list requires O(n) space.
          - The recursion depth in DFS is at most O(n) in the worst case.
          - The visited set takes O(n) space.
        """ 
        restricted_set = set(restricted)
        
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        # Step 2: Use DFS to count reachable nodes while avoiding restricted nodes
        def dfs(node, visited):
            visited.add(node)
            count = 1 # Count the current node
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in restricted_set:
                    count += dfs(neighbor, visited)
            return count
        
        # Start DFS from node 0
        return dfs(0, set())
