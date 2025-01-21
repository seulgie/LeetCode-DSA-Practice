class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Returns the number of distinct ways to climb a staircase of n steps.
        
        :param n: int - Number of steps in the staircase
        :return: int - Number of distinct ways to climb the staircase
        
        Time Complexity:
        - O(n): We compute f(2) through f(n) iteratively.
        
        Space Complexity:
        - O(1): We use only two variables to store intermediate results.
        """
        
        if n<=1:
            return 1
        
        # Initialize variables for the first two steps
        prev1, prev2 = 1, 1
        
        # Compute f(2) to f(n)
        for _ in range(2, n+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1
