from collections import deque

def updateMatrix(mat):
    """
    Given an m x n binary matrix mat, finds the distance of the nearest 0 for each cell.
    
    Approach:
    - Uses BFS starting from all `0` cells simultaneously.
    - Each `1` cell's distance is updated based on its nearest `0`.
    
    Complexity Analysis:
    - **Time Complexity:** O(m * n), since each cell is processed at most once.
    - **Space Complexity:** O(m * n), due to the queue storing matrix elements.
    """
    
    rows, cols = len(mat), len(mat[0])
    queue = deque()
    
    # Step 1: Initialize distances and add all `0`s to queue
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                queue.append((r, c))  # Start BFS from '0' cells
            else:
                mat[r][c] = float('inf')  # Mark '1's as unprocessed
    
    directions = [(0,1), (0,-1), (1,0), (-1,0)]  # Right, Left, Down, Up
    
    # Step 2: Perform BFS
    while queue:
        r, c = queue.popleft()  # Process current cell
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] > mat[r][c] + 1:
                mat[nr][nc] = mat[r][c] + 1  # Update shortest distance
                queue.append((nr, nc))  # Add updated cell to queue
    
    return mat
