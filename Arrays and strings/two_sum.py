def has_pair_with_sum(nums, target):
    left, right = 0, len(nums) - 1  # Initialize pointers
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:  # Found the pair
            return True
        elif current_sum < target:  # Increase the sum
            left += 1
        else:  # Decrease the sum
            right -= 1
    
    return False  # No pair found
