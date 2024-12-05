class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n * (n+1) // 2
        
        return total_sum - sum(nums)
    
    # Time complexity : O(n) since we iterate through the array once to compute the sum
    # Space complexity : O(1) as no additional data structures are used.
