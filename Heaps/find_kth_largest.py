class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Returns the kth largest element in the array.
        
        :param nums: List[int] - Input array
        :param k: int - The kth largest position
        :return: int - The kth largest element
        
        Time Complexity:
        - O(n log k): n is the length of nums, and log k is the cost of heap operations.
        
        Space Complexity:
        - O(k): For storing the heap.
        """
        # Step 1: Initialize a min-heap
        min_heap = []
        
        # Step 2: Process each number in nums
        for num in nums:
            heapq.heappush(min_heap, num) # Push current number into the heap
            if len(min_heap) > k: # Ensure heap size does not exceed k
                heapq.heappop(min_heap) # Remove the smallest element
                
        # Step 3: The root of the heap is the kth largest element
        return min_heap[0]
