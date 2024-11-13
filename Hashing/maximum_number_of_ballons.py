from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Set the initial values as 0 using defaultdict
        letter_freq = defaultdict(int)
        for letter in text:
            letter_freq[letter] += 1
            
        # Find each letter's freq
        a_count = letter_freq.get('a',0)
        b_count = letter_freq.get('b',0)
        l_count = letter_freq.get('l',0) // 2
        o_count = letter_freq.get('o',0) // 2
        n_count = letter_freq.get('n',0)
        
        return min(a_count, b_count, l_count, o_count, n_count)
