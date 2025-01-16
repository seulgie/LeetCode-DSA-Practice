class StockSpanner:
    def __init__(self):
        """
        Initialize the StockSpanner object.
        We use a stack to store (price, span) pairs.
        """
        self.stack = []  # Stack to store (price, span) pairs

    def next(self, price: int) -> int:
        """
        Return the span of the stock's price for the current day.

        Time Complexity:
        - Amortized O(1): Each price is pushed and popped from the stack once.
        - Worst-case per operation: O(n), where n is the number of prices.

        Space Complexity:
        - O(n): Stack stores prices and their spans.

        :param price: The price of the stock for the current day.
        :return: The span of the stock's price.
        """
        span = 1  # Start with a span of 1 for the current day

        # Merge spans for prices that are less than or equal to the current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]  # Add the span of the popped price

        # Push the current price and its span onto the stack
        self.stack.append((price, span))

        return span
