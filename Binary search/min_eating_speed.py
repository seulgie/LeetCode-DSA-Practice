from math import ceil

def minEatingSpeed(piles, h):
    # Binary search for minimum k
    """
    Time Complexity: O(n * max(piles))
    """
    left, right = 1, max(piles)
    
    def canFinish(k):
        """Check if Koko can finish all bananas in h hours with eating speed k."""
        total_hours = sum(ceil(pile / k) for pile in piles)
        return total_hours <= h

    while left < right:
        mid = (left + right) // 2
        if canFinish(mid):
            right = mid  # Try a smaller k
        else:
            left = mid + 1  # Increase k

    return left

# Example Test Case:
piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))  # Output: 4
