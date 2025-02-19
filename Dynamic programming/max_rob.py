from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        This function uses recursion with memoization to find the maximum amount of money 
        that can be robbed from houses without alerting the police.
        
        Memoization is used to store previously computed results, avoiding redundant calculations
        and optimizing the recursive approach from O(2^n) (exponential) to O(n) (linear).
        """
        def dp(i):
            # Base cases
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            # If the result is already computed, return it
            if i in memo:
                return memo[i]
            
            # Recurrence relation: choose to rob current house or skip it
            memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
            return memo[i]
        
        memo = {}  # Dictionary to store computed results for memoization
        return dp(len(nums) - 1)

    """
    Complexity Analysis:
    - Time Complexity: O(n), since each subproblem is computed once and stored in memo.
    - Space Complexity: O(n), due to recursion stack and memo dictionary storing n results.
    """
