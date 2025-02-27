def dailyTemperatures(temperatures):
    """
    Time Complexity: O(n)
    - Each element is pushed and popped from the stack at most once.
    Space Complexity: O(n)
    - Stack stores indices, which in the worst case can be O(n).
    - The answer array is O(n).
    """
    n = len(temperatures)
    answer = [0] * n
    stack = []  # Stores indices of temperatures

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
        stack.append(i)  # Push current index onto the stack

    return answer
