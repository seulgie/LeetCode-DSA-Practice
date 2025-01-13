def findSmallestSetOfVertices(n, edges):
    """
    Find the smallest set of vertices to reach all nodes in a directed acyclic graph.

    Time Complexity:
    - O(m + n): Where m is the number of edges and n is the number of vertices.
      Iterating through the edges takes O(m), and checking all vertices takes O(n).
    
    Space Complexity:
    - O(n): To store the set of nodes with incoming edges.

    :param n: Number of vertices
    :param edges: List[List[int]] - List of directed edges [x, y]
    :return: List[int] - Smallest set of vertices to reach all nodes
    """
    # Initialize a set to keep track of nodes with incoming edges
    has_incoming = set()

    # Mark all nodes with incoming edges
    for _, y in edges:
        has_incoming.add(y)

    # Nodes without incoming edges are the result
    result = [node for node in range(n) if node not in has_incoming]
    
    return result
