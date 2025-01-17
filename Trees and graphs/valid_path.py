class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Determine if there is a valid path from source to destination in a graph.
        
        :param n: int - Number of vertices in the graph (0 to n-1)
        :param edges: List[List[int]] - List of edges representing the graph
        :param source: int - Starting vertex
        :param destination: int - Target vertex
        :return: bool - True if a valid path exists, False otherwise
        
        Time Complexity:
        - O(V + E): V is the number of vertices, and E is the number of edges.
        
        Space Complexity:
        - O(V + E): For the adjacency list and the recursion stack.
        """
        from collections import defaultdict
        
        # Step 1: Build the graph using an adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # Step 2: Perform DFS
        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, visited):
                        return True
            return False
        
        # Step 3: Initialize visited set and start DFS
        visited = set()
        return dfs(source, visited)
