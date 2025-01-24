class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        """
        Finds the maximum total sweetness of the piece you can get
        after optimally cutting the chocolate bar.
        
        :param sweetness: List[int] - Sweetness values of each chunk
        :param k: int - Number of friends (requires k cuts)
        :return: int - Maximum sweetness of the piece you can get
        
        Time Complexity:
        - O(n log m), where n is the length of the sweetness array, and m is the total sum of sweetness.
          - Binary search runs in O(log m).
          - For each mid value during the binary search, we check the partition feasibility in O(n).
          
        Space Complexity:
        - O(1): No additional space is used.
        """
        
        def canDivide(mid):
            """
            Checks if it's possible to divide the chocolate into k + 1 pieces
            such that each piece has at least 'mid' sweetness.
            """
            current_sum = 0
            pieces = 0
            for s in sweetness:
                current_sum += s
                if current_sum >= mid:
                    pieces += 1
                    current_sum = 0
            return pieces >= k + 1
        
        # Binary search range
        left, right = 1, sum(sweetness) // (k + 1)
        
        while left < right:
            mid = (left + right + 1) // 2
            if canDivide(mid):
                left = mid # Try for larger minimum sweetness
            else:
                right = mid - 1
                
        return left
