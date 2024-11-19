def findMaxLength(nums):
    # Transform 0s to -1s and use a hashmap to track cumulative sums
    hashmap = {0: -1}  # To handle the case when subarray starts from index 0
    max_length = 0
    cumulative_sum = 0
    
    for i, num in enumerate(nums):
        # Update cumulative_sum
        cumulative_sum += 1 if num == 1 else -1
        
        # Check if cumulative_sum exists in hashmap
        if cumulative_sum in hashmap:
            # Calculate the length of the subarray
            max_length = max(max_length, i - hashmap[cumulative_sum])
        else:
            # Store the first occurrence of this cumulative_sum
            hashmap[cumulative_sum] = i
    
    return max_length
