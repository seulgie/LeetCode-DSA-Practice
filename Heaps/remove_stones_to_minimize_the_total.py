from heapq import heappush, heappop, heapify

def min_stone_sum(piles, k):
    """
    Function to minimize the total number of stones after k operations.

    Parameters:
    piles (List[int]): List of integers representing the number of stones in each pile.
    k (int): Number of operations to perform.

    Returns:
    int: Minimum possible total number of stones remaining.
    """

    # Step 1: Convert the list into a max heap (negate values to use Python's min heap as max heap)
    max_heap = [-pile for pile in piles]
    heapify(max_heap)  # O(n)

    # Step 2: Perform k operations
    for _ in range(k):  # O(k)
        # Pop the largest pile (smallest negative value)
        largest_pile = -heappop(max_heap)  # O(log n)

        # Reduce the pile size
        reduced_pile = largest_pile - largest_pile // 2

        # Push the updated pile back into the heap
        heappush(max_heap, -reduced_pile)  # O(log n)

    # Step 3: Calculate the total number of stones remaining
    return -sum(max_heap)  # O(n)

# Complexity Analysis:
# --------------------
# 1. Heap Initialization: O(n)
#    - `heapify` rearranges the list into a valid heap.
# 2. Perform k Operations: O(k * log n)
#    - Each operation involves a pop (O(log n)) and a push (O(log n)), repeated k times.
# 3. Summing Remaining Stones: O(n)
#    - Summing all elements in the heap to compute the total.
#
# Total Complexity: O(n + k * log n)
