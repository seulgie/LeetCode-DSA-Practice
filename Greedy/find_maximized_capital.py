import heapq

def findMaximizedCapital(k, w, profits, capital):
   """
   Time Complexity: O(n log n + k log n)
     - Sorting projects: O(n log n)
     - Heap operations: O(k log n) in worst case
     - Overall: O(n log n) (since k <= n)

   Space Complexity: O(n)
     - Storing sorted projects: O(n)
     - Heap storage: O(n) in worst case
   """
   # Step 1: Sort projects based on required capital
   projects = sorted(zip(capital, profits))

   max_heap = [] # Max heap to store available projects (profit as key)
   i = 0 # Pointer to track sorted projects

   # Step 2: Iterate for k projects
   for _ in range(k):
      # Step 3: Push all projects we can afford into max-heap
         while i < len(projects) and projects[i][0] <= w:
            heapq.heappush(max_heap, -projects[i][1]) # Store profits as negative (max-heap)
            i += 1

      # Step 4: Pick the most profitable project
      if not max_heap:
         break   # No more affordable projects

      w += -heapq.heappop(max_heap)  # Increase capital

   return w
