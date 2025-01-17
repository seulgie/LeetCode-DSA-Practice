class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        Returns the maximum size of a subsequence such that the sum of its elements
        is less than or equal to each query in queries.
        
        :param nums: List[int] - Array of integers
        :param queries: List[int] - Array of queries
        :return: List[int] - Maximum sizes of subsequences for each query
        
        Time Complexity:
        - O(n log n + m * n): n log n for sorting nums, m queries processed in O(n) each.
        
        Space Complexity:
        - O(n): For the prefix sums array.
        """
        # Step 1: Sort nums
        nums.sort()
        
        # Step 2: Compute prefix sums
        n = len(nums)
        prefix_sums = [0] * n
        prefix_sums[0] = nums[0]
        for i in range(1, n):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i]
            
        # Step 3: Process each query
        result = []
        for query in queries:
            # Find the largest index where prefix_sums[index] <= query
            count = 0
            current_sum = 0
            for num in nums:
                if current_sum + num <= query:
                    current_sum += num
                    count += 1
                else:
                    break
            result.append(count)
                
        return result
        
        
        
