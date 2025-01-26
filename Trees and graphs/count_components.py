class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Returns the number of connected components in the graph.
        
        :param n: int - Number of nodes
        :param edges: List[List[int]] - List of edges
        :return: int - Number of connected components
        
        Time Complexity:
        - O(n + e): Where n is the number of nodes and e is the number of edges.
          - We visit every node and traverse all edges once during the DFS.
          
        Space Complexity:
        - O(n + e): Space required for the adjacency list.
        - O(n): Additional space for the visited set.
        """
        
        # Build adjacency list
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        # Keep track of visited nodes
        visited = set()
        
        def dfs(node):
            # Perform DFS and mark all connected nodes as visited
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
                    
        components = 0
        
        # Iterate through all nodes
        for i in range(n):
            if i not in visited:
                components += 1 # New connected component found
                dfs(i) # Explore the entire connected component
                
        return components
    
