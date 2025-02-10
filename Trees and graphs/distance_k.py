from collections import defaultdict, deque

def distanceK(root, target, k):
    # Step 1: Build Graph using DFS
    graph = defaultdict(list)

    def buildGraph(node, parent=None):
        if not node:
            return
        if parent:
            graph[node.val].append(parent.val)
            graph[parent.val].append(node.val)
        buildGraph(node.left, node)
        buildGraph(node.right, node)

    buildGraph(root)

    # Step 2: BFS from target to find nodes at distance K
    queue = deque([(target.val, 0)])  # (node, distance)
    visited = set()
    visited.add(target.val)

    while queue:
        node, dist = queue.popleft()

        if dist == k:  # If distance is K, collect all remaining nodes
            return [node for node, _ in queue] + [node]

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return []
