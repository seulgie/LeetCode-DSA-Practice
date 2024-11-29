# **Heap: A Priority Queue Implementation**

## **Overview**
A **heap** is a powerful data structure used to efficiently manage elements based on priority. It supports quick access to the **smallest** or **largest** element and is commonly used to implement a **priority queue**.

### **Key Operations**
| Operation                  | Time Complexity |
|----------------------------|-----------------|
| Add an element             | \(O(\log n)\)   |
| Remove the min/max element | \(O(\log n)\)   |
| Find the min/max element   | \(O(1)\)        |

Heaps are classified as:
- **Min Heap**: Retrieves the smallest element.
- **Max Heap**: Retrieves the largest element.

---

## **Why Use a Heap?**
Heaps drastically improve time complexity for repeated max/min operations.
Python's `heapq` supports heaps with minimal setup, ideal for sorting, scheduling, and graph problems.
- **Sorting**: Efficiently sort elements using Heap Sort (\(O(n \cdot \log n)\)).
- **Graph Algorithms**: E.g., Dijkstra’s shortest path algorithm.
- **Priority Scheduling**: Managing tasks based on priority.

---

## **Heap Implementation**

### **Binary Heap**
The most common heap implementation is the **binary heap**, represented as a **complete binary tree** stored in an array:
- **Parent-Child Relationships**:
  - **Left Child**: \(2i + 1\)
  - **Right Child**: \(2i + 2\)
  - **Parent**: \(\lfloor (i-1)/2 \rfloor\)

### **Heapify Operations**
1. **Bubble Up**: Adjusts positions when adding an element.
2. **Bubble Down**: Restores the heap after removing the root.

These operations ensure logarithmic complexity.

---

## **Using Heaps in Python**

Python provides a built-in module, `heapq`, for heap operations.

### **Basic Operations**
```python
from heapq import heappush, heappop, heapify

# Initialize a heap
heap = []

# Add elements
heappush(heap, 10)
heappush(heap, 5)
heappush(heap, 20)

# Access the smallest element
print(heap[0])  # Output: 5

# Remove the smallest element
print(heappop(heap))  # Output: 5
