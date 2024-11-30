def is_valid(s: str) -> bool:
    """
    Determines if the input string containing brackets is valid.
    
    Args:
        s (str): The input string containing '(', ')', '{', '}', '[' and ']'.
    
    Returns:
        bool: True if the string is valid, False otherwise.
    """
    # Stack to keep track of opening brackets
    stack = []
    # Mapping of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}

    # Iterate through each character in the string
    for char in s:
        if char in bracket_map:  # If the character is a closing bracket
            # Pop from stack or use a dummy value if the stack is empty
            top_element = stack.pop() if stack else '#'
            # Check if the popped element matches the expected opening bracket
            if bracket_map[char] != top_element:
                return False
        else:  # If the character is an opening bracket
            stack.append(char)

    # The string is valid if the stack is empty at the end
    return not stack


# Example Usage
if __name__ == "__main__":
    test_cases = [
        "({})",    # Valid
        "(){}[]",  # Valid
        "(]",      # Invalid
        "({)}",    # Invalid
        "",        # Valid (empty string)
        "["        # Invalid
    ]
    
    for test in test_cases:
        print(f"Input: {test}, Is Valid: {is_valid(test)}")

"""
Complexity Analysis:
--------------------

Time Complexity: O(n)
- Each character in the string is processed once. Stack operations (push and pop) are O(1), 
  resulting in a total time complexity proportional to the length of the string.

Space Complexity: O(n)
- In the worst case, the stack contains all opening brackets in the string, 
  leading to O(n) space usage.
"""
