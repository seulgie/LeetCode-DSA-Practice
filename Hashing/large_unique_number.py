class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # Count frequencies using defaultdict
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        
        # Iterate through the keys in descending order to find the largest unique number
        for num in sorted(frequency.keys(), reverse=True):
            if frequency[num] == 1:
                return num
        
        # If no unique number exists, return -1
        return -1
