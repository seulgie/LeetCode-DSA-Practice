def ways_to_split(nums):
    """
    Finds the number of ways to split the array into two parts such that
    the sum of the first section is greater than or equal to the sum of the second section.

    Args:
        nums (List[int]): The input integer array.

    Returns:
        int: The number of valid ways to split the array.

    Complexity:
        Time Complexity:
            - Computing the prefix sum takes O(n).
            - Iterating through the array to calculate the split conditions takes O(n).
            - Overall time complexity is O(n).
        Space Complexity:
            - The prefix sum array requires O(1) space.
    """
    n = len(nums)
    if n < 2:
        return 0

    # Calculate prefix sum
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    total_sum = prefix_sum[-1]
    count = 0

    # Iterate through the array to determine valid splits
    for i in range(n - 1):  # The split ensures the second section has at least one number
        sum_left = prefix_sum[i]
        sum_right = total_sum - sum_left

        if sum_left >= sum_right:
            count += 1

    return count
