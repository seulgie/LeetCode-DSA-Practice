from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        """
        Given an integer array arr, this function returns the minimum size of the set
        so that at least half of the integers of the array are removed.
        
        :param arr: List[int] - The input array of integers.
        :return: int - The minimum size of the set.
        """
        # Step 1: Count the frequency of each integer in the array
        freq = Counter(arr)
        
        # Step 2: Sort frequencies in descending order
        frequencies = sorted(freq.values(), reverse=True)
        
        # Step 3: Greedily select numbers with the highest frequencies until at least half are removed
        total_removed = 0
        set_size = 0
        half_size = len(arr) // 2
        
        for count in frequencies:
            total_removed += count
            set_size += 1
            if total_removed >= half_size:
                break
                
        return set_size
    
# Example usage
if __name__ == "__main__":
    arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
    print("Minimum set size:", minSetSize(arr)) # Output: 2
    
"""
1. Time Complexity:
   - Counting frequencies using Counter takes O(n), where n is the size of the array.
   - Sorting the frequency values takes O(k log k), where k is the number of unique elements in the array.
   - Iterating over the sorted frequencies takes O(k).
   Overall Time Complexity: O(n + k log k), where k <= n. In the worst case, this simplifies to O(n log n)).
   
2. Space Complexity:
   - The Counter object stores the frequencies of elements, taking O(k) space.
   - The sorted list of frequencies also takes O(k) space.
   Overall Space Complexity: O(k), where k is the number of unique elements.
"""
