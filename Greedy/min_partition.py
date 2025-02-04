def minPartitions(nums, k):
  nums.sort() # Step 1: Sort the array
  count = 0
  i = 0
  n = len(nums)

  while i < n:
    count += 1 # Start a new subsequence
    min_element = nums[i] # Smallest element in current subsequence

    # Expand subsequence while max difference <= k
    while i < n and nums[i] - min_element <= k:
      i += 1 # Move to next element

  return count
