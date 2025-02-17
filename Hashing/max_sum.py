def maxSum(nums):
    """
    Finds the maximum sum of a pair of numbers with the same digit sum.

    Approach:
    - Use a dictionary to store the maximum number for each digit sum.
    - Iterate through the array, compute digit sums, and check for existing matches.
    - Update the maximum sum if a valid pair is found.

    Complexity Analysis:
    - **Time Complexity:** O(n log M), where `n` is the size of `nums` and `M` is the largest number (log M for digit sum computation).
    - **Space Complexity:** O(n), as we store up to `n` digit sums in a dictionary.
    """
    
    def digit_sum(n):
        """Helper function to compute the sum of digits of a number."""
        return sum(int(d) for d in str(n))

    digit_sum_map = {}  # Stores the largest number for each digit sum
    max_pair_sum = -1  # Initialize result to -1

    for num in nums:
        d_sum = digit_sum(num)

        if d_sum in digit_sum_map:
            max_pair_sum = max(max_pair_sum, num + digit_sum_map[d_sum])  # Compare with existing max sum
            digit_sum_map[d_sum] = max(digit_sum_map[d_sum], num)  # Store the larger number
        else:
            digit_sum_map[d_sum] = num  # Store first occurrence

    return max_pair_sum

# Example Usage:
nums = [51, 71, 17, 42]
print(maxSum(nums))  # Output: 93 (51 + 42)
