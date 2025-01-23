import math

def smallestDivisor(nums, threshold):
    """
    Finds the smallest divisor such that the sum of the division results
    (rounded up) is less than or equal to the threshold.

    :param nums: List[int] - Array of integers
    :param threshold: int - Threshold for the division sum
    :return: int - Smallest divisor

    Time Complexity:
    - O(n log m), where n is the size of the array and m is the maximum number in nums.
      - Binary search runs in O(log m).
      - For each mid value during the binary search, the sum of division results is computed in O(n).

    Space Complexity:
    - O(1): No additional space is used except for a few variables.
    """
    def division_sum(divisor):
        # Helper function to calculate the sum of nums[i] / divisor (rounded up)
        return sum(math.ceil(num / divisor) for num in nums)

    # Binary search for the smallest divisor
    left, right = 1, max(nums)
    while left < right:
        mid = (left + right) // 2
        if division_sum(mid) > threshold:
            left = mid + 1  # Increase divisor to reduce the sum
        else:
            right = mid  # Try smaller divisors

    return left

# Example Usage:
# nums = [1, 2, 5, 9]
# threshold = 6
# print(smallestDivisor(nums, threshold)) # Output: 5

