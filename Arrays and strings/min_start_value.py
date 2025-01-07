class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        """
        Given an array of integers nums, this function returns the minimum positive value of startValue
        such that the step-by-step sum of startValue plus elements in nums is never less than 1.
        
        :param nums: List[int] - The input array of integers.
        :return: int - The minimum positive value of startValue.
        """
        # Calculate the prefix sum and track the minimum value encountered
        prefix_sum = 0
        min_prefix_sum = 0
        
        for num in nums:
            prefix_sum += num
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            
        # To ensure the step-by-step sum is never less than 1,
        # the startValue must offset the negative minimum prefix sum.
        return 1 - min_prefix_sum


"""
1. Time Complexity:
   - The function iterates through the nums array once to compute the prefix sum and minimum prefix sum.
   - Time complexity: O(n), where n is the length of the array.
   
2. Space Complexity:
   - O(1): The function uses a constant amount of additional space
"""
