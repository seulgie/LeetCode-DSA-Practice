from typing import List

def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
  """
  Returns the number of successful potion pairs for each spell.

  :param spells: List[int] - Strength of each spell
  :param potions: List[int] - Strength of each potion
  :param success: int - Minimum product for success
  :return: List[int] - Number of successful pairs for each spell

  Time Complexity:
  - O(n log n + m log m): Sorting the potions takes O(m log m), and for each spell (n times),
    a binary search (O(log m)) is performed.

  Space Complexity:
  - O(n + m): Space for the output array and sorted potions.
  """
  # Sort potions for binary search
  potions.sort()

  def count_successful_pairs(spell):
    # Find the smallest index where spell * potions[index] >= success
    left, right = 0, len(potions)
    while left < right:
      mid = (left + right) // 2
      if spell * potions[mid] >= success:
        right = mid
      else:
        left = mid + 1
      return len(potions) - left

 # Count successful pairs for each spell
 return [count_successful_pairs(spell) for spell in spells]

  
