from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        BFS approach to find the shortest path to the nearest exit in a maze.
        """
        rows, cols = len(maze), len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        queue = deque()
        queue.append((entrance[0], entrance[1], 0))  # (row, col, steps)
        maze[entrance[0]][entrance[1]] = '+'  # Mark entrance as visited
        
        while queue:
            cell = queue.popleft()
            r, c, steps = cell  # Ensure proper unpacking
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
                    # Check if it's an exit (border cell that is not entrance)
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        return steps + 1
                    
                    # Mark as visited and enqueue
                    maze[nr][nc] = '+'
                    queue.append((nr, nc, steps + 1))
        
        return -1  # No exit found
    
    """
    Complexity Analysis:
    - Time Complexity: O(m * n), as we may visit every cell in the worst case.
    - Space Complexity: O(m * n), for the queue in the worst case if all cells are open.
    """
