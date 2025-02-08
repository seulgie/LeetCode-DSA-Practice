from collections import deque

def shortestPathBinaryMatrix(grid):
    """
    Time Complexity: O(n^2) - In the worst case, we visit all cells in the matrix.
    Space Complexity: O(n^2) - Due to the queue storing visited cells.
    """
    n = len(grid)
    
    # Edge case: Start or end blocked
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1
    
    # Possible moves in 8 directions
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    # BFS setup: Queue stores (row, col, path_length)
    queue = deque([(0, 0, 1)])
    grid[0][0] = 1  # Mark as visited
    
    while queue:
        r, c, path_length = queue.popleft()
        
        # If we reached the bottom-right corner, return the shortest path
        if r == n - 1 and c == n - 1:
            return path_length
        
        # Explore all 8 directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                queue.append((nr, nc, path_length + 1))
                grid[nr][nc] = 1  # Mark as visited

    return -1  # No path found
