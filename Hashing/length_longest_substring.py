class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.
        
        Time Complexity:
          - O(n): Each character is added and removed from the hash set at most once.
          
        Space Complexity:
          - O(min(n, a)): Where n is the length of the string and a is the size of the character set
          
        :param s: Input string
        :return: Length of the longest substring without repeating characters
        """
        char_set = set() # Hash set to track characters in the current window
        left = 0 # left pointer of the sliding window
        max_length = 0 # store the maximum length of substring
        
        for right in range(len(s)):
            # If the character is already in the set, shrink the window
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                
            # Add the current character to the set
            char_set.add(s[right])
            
            # Update the maximum Length
            max_length = max(max_length, right - left + 1)
            
        return max_length
    
