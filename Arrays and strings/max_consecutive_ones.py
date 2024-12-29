def maxConsecutiveOnes(nums, k):
    """
    Find the maximum number of consecutive 1's in the binary array
    if you can flip at most k 0's.

    Time Complexity:
    - O(n): We traverse the array once with a sliding window.
    
    Space Complexity:
    - O(1): No extra space is used apart from variables.

    :param nums: List[int] - Binary array of 0's and 1's
    :param k: int - Maximum number of 0's that can be flipped
    :return: int - Maximum consecutive 1's after at most k flips
    """
    left = 0  # Left pointer for the sliding window
    max_length = 0  # To store the result
    zeros_count = 0  # To count the number of 0's in the current window

    for right in range(len(nums)):
        # Expand the window by including nums[right]
        if nums[right] == 0:
            zeros_count += 1

        # If there are more than k 0's, shrink the window from the left
        while zeros_count > k:
            if nums[left] == 0:
                zeros_count -= 1
            left += 1

        # Update the maximum length of the window
        max_length = max(max_length, right - left + 1)

    return max_length
