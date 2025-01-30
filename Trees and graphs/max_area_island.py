class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Returns the maximum area of an island in the given binary grid.
        
        :param grid: List[List[int]] - Binary matrix where 1 represents land and 0 represents water.
        :return: int - The maximum island area found.
        
        Time Complexity:
        - O(m * n): We visit each cell at most once.
        
        Space Complexity:
        - O(m * n): In the worst case, the recursion stack can go up to m * n deep.
        """
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        
        def dfs(r, c):
            """Performs DFS to explore the island and calculate its area."""
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0 # Mark the cell as visited
            area = 1
            
            # Explore 4-directionally
            area += dfs(r + 1, c) # Down
            area += dfs(r - 1, c) # Up
            area += dfs(r, c + 1) # Right
            area += dfs(r, c - 1) # Left
            
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
                
                
        return max_area
    
