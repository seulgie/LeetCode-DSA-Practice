from collections import deque

def maxSlidingWindow(nums, k):
    """
    Time Complexity: O(n)
    - Each element is pushed/popped at most once → O(n).
    Space Complexity: O(k)
    - Deque stores at most k elements at any time.
    """
    n = len(nums)
    if n * k == 0: 
        return []
    
    result = []
    dq = deque()  # Store indices

    for i in range(n):
        # Remove indices out of the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove elements smaller than the current element from the back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        # Add the current element index
        dq.append(i)

        # Store the maximum for the current window
        if i >= k - 1:
            result.append(nums[dq[0]])  # Max element is at deque[0]
    
    return result
