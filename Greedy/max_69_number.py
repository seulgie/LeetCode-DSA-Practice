class Solution:
    def maximum69Number (self, num: int) -> int:
        """
        This function takes a positive integer 'num' consisting only of digits 6 and 9.
        It returns the maximum number obtainable by changing at most one digit (6 to 9 or 9 to 6)
        """
        # Convert the number to a list of characters for easier manipulation
        num_list = list(str(num))
        
        # Traverse the digits
        for i in range(len(num_list)):
            # Change the first occurence of '6' to '9' and break
            if num_list[i] == '6':
                num_list[i] = '9'
                break
                
        # Join the list back into a string and convert to integer
        return int(''.join(num_list))
    
    # Complexity Analysis:
    # Time Complexity: O(n), we traverse the digits of the number once to find the first '6' to change.
    # Space Complexity: O(n), converting the number to a string and storing its characters in a list
