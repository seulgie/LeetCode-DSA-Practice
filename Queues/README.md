# Queue Data Structure

## Overview
A **Queue** is a data structure that follows the **FIFO** (First In, First Out) principle. Elements are added at one end (enqueue) and removed from the opposite end (dequeue). 

### Real-World Examples:
- **Physical Queue**: A line at a fast-food restaurant.
- **Software Example**: Print jobs in a printer queue.

### Key Operations:
- **Enqueue**: Add an element to the back.
- **Dequeue**: Remove an element from the front.

---

## Implementation
Queues can be implemented using:
1. **Dynamic Arrays**: Simple, but front operations take \( O(n) \).
2. **Doubly Linked List**: Efficient with \( O(1) \) enqueue and dequeue operations.

---

## Python Example Using `collections.deque`
The `deque` (double-ended queue) from Python's `collections` module is ideal for queue implementations.

### Code Example:
```python
import collections

# Initialize an empty queue
queue = collections.deque()

# Initialize with values
queue = collections.deque([1, 2, 3])

# Enqueue (add elements)
queue.append(4)
queue.append(5)

# Dequeue (remove elements)
queue.popleft()  # Removes 1
queue.popleft()  # Removes 2

# Access front element
front = queue[0]  # 3

# Check size
size = len(queue)  # 3
