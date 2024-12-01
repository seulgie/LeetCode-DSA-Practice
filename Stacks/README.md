# Understanding Stacks

A **stack** is an ordered collection of elements where elements are added and removed only from the same end. This structure follows the **LIFO** (Last In, First Out) principle, where the last element added to the stack is the first one to be removed. 

## Real-World Analogy

A common example is a stack of plates in a kitchen:
- You add plates to the top of the stack.
- You remove plates from the top of the stack.

Similarly, in the software world:
- A browser's tab history works like a stack. For example:
  1. Start on site A.
  2. Click a link to go to site B.
  3. Click another link to go to site C.

The browser history now looks like this: `[A, B, C]`.  
Click the back arrow:
- Once: History is `[A, B]`.
- Twice: History is `[A]`.

## Operations on a Stack

- **Push**: Add an element to the top of the stack.
- **Pop**: Remove the top element from the stack.
- **Peek**: View the top element without removing it.



## Complexity of Basic Stack Operations

| Operation | Time Complexity | Explanation |
|-----------|------------------|-------------|
| Push      | O(1)             | Adding an element to the top is a constant-time operation. |
| Pop       | O(1)             | Removing the top element is a constant-time operation. |
| Peek      | O(1)             | Viewing the top element does not require iteration. |



In Python, stacks can be implemented using a list:
```python
stack = []
stack.append(element)  # Push
stack.pop()           # Pop
