from collections import defaultdict

def groupAnagrams(strs):
    """
    Groups anagrams together.

    Approach:
    - Use a hashmap where the key is the sorted version of each string.
    - Append original strings to the respective key.
    - Return all values of the hashmap as the result.

    Complexity Analysis:
    - **Time Complexity:** O(n * k log k) 
      - Sorting each word takes O(k log k), where k is the word length.
      - Inserting into hashmap is O(1).
    - **Space Complexity:** O(n * k) 
      - Stores n words with length up to k in a hashmap.
    """
    
    anagram_groups = defaultdict(list)  # Dictionary with default list
    
    for word in strs:
        sorted_word = "".join(sorted(word))  # Sorting takes O(k log k)
        anagram_groups[sorted_word].append(word)  # Store original word
    
    return list(anagram_groups.values())  # Return grouped anagrams

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
