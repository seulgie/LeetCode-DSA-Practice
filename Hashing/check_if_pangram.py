class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Initialize an empty set to store found characters
        found_characters = set()
        
        # Iterate over each character in the string
        for char in sentence:
            # Add the character to the set (duplicates will be ignored automatically)
            found_characters.add(char)
            
        return True if len(found_characters) == 26 else False
