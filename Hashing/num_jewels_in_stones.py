class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Count the number of stones that are jewels.
        
        Time Complexity:
          - O(m + n): Where m is the length of jewels and n is the length of stones.
            Building the set of jewels takes O(m), and checking each stone takes O(n).
            
        Space Complexity:
          - O(m): The space required to store the set of jewels.
          
        :param jewels: String representing jewel types
        :param stones: String representing stone types
        :return: Number of stones that are jewels
        """
        jewel_set = set(jewels) # Create a set of jewel types for quick lookup
        count = 0 # Initialize the count of jewels in stones
        
        for stone in stones:
            if stone in jewel_set:
                count += 1
                
        return count
    
