class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Returns the minimum cost to reach the top of the staircase.
        
        :param cost: List[int] - The cost of each step
        :return: int - Minimum cost to reach the top
        
        Time Complexity:
        - O(n): We compute the result for each step once.
        
        Space Complexity:
        - O(1): We use only two variables for the iterative approach.
        """
        n = len(cost)
        if n == 2:
            return min(cost) # If there are only two steps, choose the cheaper one
        
        # Initialize the first two costs
        prev2, prev1 = cost[0], cost[1]
        
        # Compute minimum cost for each step from 2 to n
        for i in range(2, n):
            current = cost[i] + min(prev1, prev2) # Minimum cost to reach step i
            prev2, prev1 = prev1, current # Move forward in the DP
            
        # Return the minimum cost to reach the top (either from the last or second last step)
        return min(prev1, prev2)
    
