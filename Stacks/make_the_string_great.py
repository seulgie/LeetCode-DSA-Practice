class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            # Check for adjacent bad characters
            if stack and (stack[-1] == char.swapcase()):
                stack.pop() # Remove the bad pair
            else:
                stack.append(char)
        return ''.join(stack)
        
# Time Complexity: O(n), where n is the length of the input string.
# This is because each character is pushed and popped from the stack at most once.
# Space Complexity: O(n), in worst case, the stack could store all the characters of the string (e.g., when no characters are removed).
        
