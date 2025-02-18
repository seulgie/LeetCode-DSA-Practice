from collections import Counter

def equalPairs(grid):
    """
    Counts the number of pairs (R, C) where R is a row and C is a column in the grid and R == C.
    
    Approach:
    - Store each row as a tuple in a hashmap with its frequency.
    - Construct columns and check how many match existing rows in the hashmap.

    Complexity Analysis:
    - **Time Complexity:** O(n²)
      - Constructing the hashmap: O(n)
      - Checking each column: O(n²)
    - **Space Complexity:** O(n²) (to store all rows and columns).
    """
    
    row_count = Counter(tuple(row) for row in grid)  # Count occurrences of each row
    
    n = len(grid)
    count = 0

    for col in zip(*grid):  # Transpose matrix to get columns
        count += row_count[col]  # Count matching row occurrences
    
    return count

# Example usage
grid = [[3,2,1],[1,7,6],[2,7,7]]
print(equalPairs(grid))  # Output: 1
