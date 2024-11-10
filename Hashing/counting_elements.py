class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        # Use a set to store all unique elements in the array
        unique_elements = set(arr)
        
        # Loop through the original array and count-valid elements
        valid_count = 0
        for element in arr:
            if element + 1 in unique_elements:
                valid_count += 1
                
        return valid_count
