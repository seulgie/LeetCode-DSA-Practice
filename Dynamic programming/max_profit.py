class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        Returns the maximum profit that can be achieved considering the transaction fee.
        
        :param prices: List[int] - Prices of stock on each day
        :param fee: int - The transaction fee per transaction
        :return: int - Maximum  profit possible
        
        Time Complexity:
        - O(n): We iterate through the prices array once.
        
        Space Complexity:
        - O(1): We use only two variables for tracking the current state.
        """
        n = len(prices)
        if n == 0:
            return 0
        
        # Two states: "holding" means we have stock, "cash" means we do not have stock
        hold, cash = -prices[0], 0
        
        for i in range(1, n):
            hold = max(hold, cash - prices[i]) # Either keep holding or buy at prices[i]
            cash = max(cash, hold + prices[i] - fee) # Either keep cash or sell at prices[i] with fee
            
        return cash
        
