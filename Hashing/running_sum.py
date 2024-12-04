class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        # Initialize an empty list for the list
        result = []
        
        # Initialize a variable to keep track of the running sum
        cumulative_sum = 0
        
        # Loop through the elements of nums
        for num in nums:
            cumulative_sum += num # Add the current number to the cumulative sum
            result.append(cumulative_sum) # Append the cumulative sum to the result List
            
        return result
    
    # Time complexity: O(n)
    # Space complexity: O(n)
