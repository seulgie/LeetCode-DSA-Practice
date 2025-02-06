from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
      """
      Time Complexity: O(n log n)
      Space Complexity: O(n)
      """
        counts = Counter(arr)
        ordered = sorted(counts.values(), reverse=True)
        
        while k:
            val = ordered[-1]
            if val <= k:
                k -= val
                ordered.pop()
            else:
                break

        return len(ordered)
