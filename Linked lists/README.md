# Linked Lists

A **linked list** is a data structure where elements, called **nodes**, are connected via pointers. Each node contains:
1. **Data**: The actual value stored.
2. **Pointers**: References to other nodes.

## Types of Linked Lists
1. **Singly Linked List**: Each node points to the next node.
2. **Doubly Linked List**: Each node points to both the next and previous nodes.
3. **Circular Linked List**: The last node points back to the head.

---

## Advantages
- **Dynamic Size**: No need for preallocation like arrays.
- **Efficient Insert/Delete**: Operations at known positions are \(O(1)\).

## Disadvantages
- **No Random Access**: Traversing to a specific node takes \(O(n)\).
- **Extra Memory Overhead**: Each node stores pointer(s).

---

## Singly Linked List Operations

### **Insertion**
- **After a Node**:
    ```python
    def insert_after(prev_node, new_node):
        new_node.next = prev_node.next
        prev_node.next = new_node
    ```
- **At Head**:
    ```python
    def insert_at_head(head, new_node):
        new_node.next = head
        return new_node  # New head
    ```

### **Deletion**
- **After a Node**:
    ```python
    def delete_after(prev_node):
        node_to_delete = prev_node.next
        prev_node.next = node_to_delete.next
    ```
- **Head**:
    ```python
    def delete_head(head):
        return head.next
    ```

---

## Doubly Linked List Operations

### **Insertion**
- **After a Node**:
    ```python
    def insert_after(node, new_node):
        new_node.next = node.next
        new_node.prev = node
        if node.next:
            node.next.prev = new_node
        node.next = new_node
    ```
- **At Head**:
    ```python
    def insert_at_head(head, new_node):
        new_node.next = head
        if head:
            head.prev = new_node
        return new_node  # New head
    ```

### **Deletion**
- **Specific Node**:
    ```python
    def delete_node(node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
    ```
- **Head**:
    ```python
    def delete_head(head):
        new_head = head.next
        if new_head:
            new_head.prev = None
        return new_head
    ```

---

## Traversal
- **Singly Linked List**:
    ```python
    def traverse(head):
        while head:
            print(head.val)
            head = head.next
    ```
- **Doubly Linked List**:
    ```python
    def traverse_forward(head):
        while head:
            print(head.val)
            head = head.next
    def traverse_backward(tail):
        while tail:
            print(tail.val)
            tail = tail.prev
    ```

---

## Complexity Summary

| **Operation**       | **Singly Linked List** | **Doubly Linked List** |
|----------------------|------------------------|-------------------------|
| **Insertion**        | \(O(1)\) with pointer | \(O(1)\) with pointer   |
| **Deletion**         | \(O(1)\) with pointer | \(O(1)\) with pointer   |
| **Traversal**        | \(O(n)\)              | \(O(n)\) (both directions) |
| **Memory**           | Less overhead         | More overhead (extra pointers) |

---

## Use Cases
- Singly Linked List: **Stacks, Queues**
- Doubly Linked List: **Deque, Browser History**
- Circular Linked List: **Task Scheduling**
