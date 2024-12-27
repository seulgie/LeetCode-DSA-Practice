class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        """
        Given a list of apple weights, return the maximum number of apples
        that can be put in a basket with a weight limit of 5000 units.
        
        Time Complexity:
          - Sorting takes O(n log n), where n is the number of apples.
          - Iterating through the sorted list takes O(n).
          - Overall Time Complexity: O(n log n).
          
        Space Complexity:
          - O(1), as we use only a few extra variables to track the count and current weight.
        """
        
        weight_limit = 5000
        weight.sort() # Sort apples by their weight in ascending order.
        
        count = 0
        total_weight = 0
        
        for w in weight:
            if total_weight + w <= weight_limit:
                total_weight += w
                count += 1
                
            else:
                break
                
        return count
