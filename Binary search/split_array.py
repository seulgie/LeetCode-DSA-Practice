class Solution:
    def splitArray(self, nums, k):
        # Helper function to check if we can split into k subarrays
        # such that no subarray's sum is greater than max_sum
        def canSplit(nums, k, max_sum):
            current_sum = 0
            subarrays = 1  # We need at least 1 subarray
            for num in nums:  # Changed 'sum' to 'num' to avoid conflict
                # If adding num exceeds max_sum, start a new subarray
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
            return True

        # Binary search for the minimized largest sum
        low = max(nums)  # The minimum possible value of the largest sum is max(nums)
        high = sum(nums)  # The maximum possible value of the largest sum is sum(nums)

        while low < high:
            mid = (low + high) // 2
            if canSplit(nums, k, mid):
                high = mid  # Try to minimize the largest sum
            else:
                low = mid + 1  # Increase the allowed largest sum

        return low
  
