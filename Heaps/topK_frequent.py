from collections import Counter
import heapq

def topKFrequent(nums, k):
    """
    Returns the k most frequent elements in the array.

    :param nums: List[int] - Array of integers
    :param k: int - Number of most frequent elements to return
    :return: List[int] - The k most frequent elements

    Time Complexity:
    - O(n + k log n): Count elements in O(n) and extract top-k in O(k log n).

    Space Complexity:
    - O(n): To store the frequency map and heap.
    """
    # Count the frequency of each element
    freq_map = Counter(nums)

    # Use a heap to find the k most frequent elements
    return heapq.nlargest(k, freq_map.keys(), key=freq_map.get)
