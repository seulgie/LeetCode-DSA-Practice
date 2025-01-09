from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given a 2D grid map of '1's (land) and '0's (water), count the number of islands.

        :param grid: List[List[str]] - A 2D grid of '1's and '0's.
        :return: int - The number of islands.
        """
        if not grid:
            return 0

        def dfs(r, c):
            # If out of bounds or at a water cell, return
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return

            # Mark the cell as visited
            grid[r][c] = "0"

            # Visit all adjacent cells
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":  # Found an unvisited land cell
                    num_islands += 1
                    dfs(r, c)  # Start DFS to mark the entire island

        return num_islands

# Example Usage
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
solution = Solution()
print(solution.numIslands(grid))  # Output: 3

"""
Complexity Analysis:

1. Time Complexity:
   - The DFS visits each cell once. Therefore, the total time complexity is O(m * n), where m is the number of rows and n is the number of columns.

2. Space Complexity:
   - The space complexity is determined by the recursion stack during the DFS. In the worst case (for example, a grid full of land), the stack can grow up to O(m * n).
   - Overall Space Complexity: O(m * n).
"""
