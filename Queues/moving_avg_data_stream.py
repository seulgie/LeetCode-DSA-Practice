class MovingAverage:

    def __init__(self, size: int):
        """
        Initializes the object with the size of the window.
        :param size: int, size of the sliding window
        """
        self.size = size
        self.window = deque()
        self.window_sum = 0
        

    def next(self, val: int) -> float:
        """
        Returns the moving average of the last 'size' values of the stream.
        :param val: int
        :return: float
        """
        # Add the new value to the window
        self.window.append(val)
        self.window_sum += val
        
        # Remove the oldest value if the window size exceeds the limit
        if len(self.window) > self.size:
            self.window_sum -= self.window.popleft()
            
        # Calculate and return the moving average
        return self.window_sum / len(self.window)
    
# Example usage
# Input
commands = ["MovingAverage", "next", "next", "next", "next"]
args = [[3], [1], [10], [3], [5]]

# Output
output = [None]
ma = MovingAverage(args[0][0]) # ma = 3
for command, arg in zip(commands[1:], args[1:]):
    if command == "next":
        output.append(ma.next(arg[0]))
        


# Complexity Analysis
# Time Complexity:
#   - The `next` function operates in O(1) time because adding an element to a deque and removing an element from the deque both take constant time.
#   - Computing the sum or maintaining it with a running total also takes O(1).
#   - Total Time Complexity: O(len(args))
# Space Complexity:
#   - The space complexity is O(size) where `size` is the maximum size of the sliding window, as the deque stores at most `size` elements.
