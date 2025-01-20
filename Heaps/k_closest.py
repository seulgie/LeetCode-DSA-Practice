class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Returns the k closest points to the origin (0, 0).
        
        :param points: List[List[int]] - List of points on the X-Y plane
        :param k: int - Number of closest points to return
        :Return: List[List[int]] - k closest points to the origin
        
        Time Complexity:
        - O(n log k): Building a max-heap for k elements takes O(log k) per insertion, and we iterate through n points.
        
        Space Complexity:
        - O(k): The heap stores up to k elements.
        """
        # Use a max-heap to store the k closest points
        max_heap = []
        
        for x, y in points:
            # Compute the square of the Euclidean distance
            distance = -(x**2 + y**2) # Negate the distance for max-heap simulation
            if len(max_heap) < k:
                heapq.heappush(max_heap, (distance, [x, y]))
            else:
                heapq.heappushpop(max_heap, (distance, [x, y]))
                
        # Extract the points from the heap
        return [point for _, point in max_heap]
    
# Example Usage:
# Points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
# k = 2
# Output: [[-2, 2], [0, 1]] (or any order)

        
