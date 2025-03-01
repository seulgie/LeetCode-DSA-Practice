from collections import deque

def longestSubarray(nums, limit):
  # Time Complexity: O(n)
  # - Each element is pushed and popped from deques at most once, so it's O(n).
  # Space Complexity: O(n)
  # - In the worst case, both deques store all elements (O(n)).
    maxDeque = deque()  # To track the maximum value
    minDeque = deque()  # To track the minimum value
    left = 0
    max_length = 0

    for right in range(len(nums)):
        # Maintain decreasing order in maxDeque
        while maxDeque and nums[maxDeque[-1]] < nums[right]:
            maxDeque.pop()
        maxDeque.append(right)

        # Maintain increasing order in minDeque
        while minDeque and nums[minDeque[-1]] > nums[right]:
            minDeque.pop()
        minDeque.append(right)

        # Shrink window if difference exceeds limit
        while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
            left += 1
            if maxDeque[0] < left:
                maxDeque.popleft()
            if minDeque[0] < left:
                minDeque.popleft()

        # Update max length
        max_length = max(max_length, right - left + 1)

    return max_length
