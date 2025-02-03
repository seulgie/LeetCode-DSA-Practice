def canDestroyAsteroids(mass, asteroids):
  """
  Time Complexity: O(n log n)
    - Sorting the asteroids takes O(n log n)
    - Iterating through the asteroids takes O(n)
    - Overall: O(n log n) due to sorting.

  Space Complexity: O(1)
    - Only a few integer variables are used.
    - No extra data structures are required.
  """
  asteroids.sort() # Step 1: Sort asteroids in ascending order

  for asteroid in asteroids: # Step 2: Try absorbing each asteroid
    if mass < asteroid:
      return False # Planet is destroyed
    mass += asteroid # Absorb the asteroid and increase mass
    
  return True # All asteroids destroyed
