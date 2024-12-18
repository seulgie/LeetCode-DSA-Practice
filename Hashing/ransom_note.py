from collections import Counter

def canConstruct(ransomNote, magazine):
    """
    Determines if ransomNote can be constructed using letters from magazine.

    Args:
        ransomNote (str): The string to construct.
        magazine (str): The string providing letters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # Count the frequency of each character in both strings
    ransom_count = Counter(ransomNote)
    magazine_count = Counter(magazine)

    # Check if magazine has enough characters for each in ransomNote
    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            return False

    return True

# Complexity Analysis:
# Time Complexity: O(N + M), where N is the length of ransomNote and M is the length of magazine.
#   - Counting characters in both strings takes O(N + M).
# Space Complexity: O(U), where U is the number of unique characters in the magazine.
#   - The space is used for storing the character counts.

# Example Usage:
if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"
    print(canConstruct(ransomNote, magazine))  # Output: True
