from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """
        Dynamic Programming approach to maximize points while respecting brainpower constraints.
        """
        n = len(questions)
        dp = [0] * (n + 1)  # DP array to store max points at each index
        
        # Process questions in reverse order (bottom-up DP)
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_question = i + brainpower + 1  # Index of next available question if we take this one
            
            # Option 1: Skip this question
            skip = dp[i + 1]
            
            # Option 2: Solve this question and add points
            take = points + (dp[next_question] if next_question < n else 0)
            
            # Store the best choice at dp[i]
            dp[i] = max(skip, take)
        
        return dp[0]  # The maximum points starting from the first question
    
    """
    Complexity Analysis:
    - Time Complexity: O(n), since we iterate through the questions once.
    - Space Complexity: O(n), as we use a DP array of size n.
    """
