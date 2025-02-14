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
    
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and mat[row][col] == 1
        
        # if you don't want to modify the input, you can create a copy at the start
        m = len(mat)
        n = len(mat[0])
        queue = deque()
        seen = set()
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col, 1))
                    seen.add((row, col))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col, steps = queue.popleft()
            
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if (next_row, next_col) not in seen and valid(next_row, next_col):
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
                    mat[next_row][next_col] = steps
        
        return mat
