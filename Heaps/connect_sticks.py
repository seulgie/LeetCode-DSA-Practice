class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        """
        Returns the minimum cost to connect all sticks into one.
        
        :param sticks: List[int] - Lengths of the sticks
        :return: int - Minimum cost to connect all sticks
        
        Time Complexity:
        - O(n log n): Heap construction takes O(n), and we perform O(n) heap operations,  each taking O(log n).
        
        Space Complexity:
        - O(n): Space required for the heap.
        """
        # Edge case: If there's only one stick, no cost is needed
        if len(sticks) == 1:
            return 0
        
        # Convert the list of sticks into a min-heap
        heapq.heapify(sticks)
        
        total_cost = 0
        
        # Combine sticks until only one stick remains
        while len(sticks) > 1:
            # Remove the two smallest sticks
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)
            
            # Combine them and calculate the cost
            cost = stick1 + stick2
            total_cost += cost
            
            # Add the new stick back into the heap
            heapq.heappush(sticks, cost)
            
        return total_cost
    
