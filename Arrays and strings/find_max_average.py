def findMaxAverage(nums, k):
    # Calculate the sum of the first window of size k
    current_sum = sum(nums[:k])
    max_sum = current_sum
    
    # Slide the window across the array
    for i in range(k, len(nums)):
        # Update the sum by subtracting the element going out and adding the one coming in
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)
    
    # Return the maximum average
    return max_sum / k
