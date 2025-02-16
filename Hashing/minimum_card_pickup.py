def minimumCardPickup(cards):
    """
    Finds the length of the shortest subarray that contains at least one duplicate.
    
    Approach:
    - Use a dictionary to store the last seen index of each card.
    - If a duplicate is found, compute the subarray length and update the minimum length.
    - If no duplicates are found, return -1.

    Complexity Analysis:
    - **Time Complexity:** O(n), since we iterate through the array once.
    - **Space Complexity:** O(n), since we store indices in a dictionary.
    """
    
    last_seen = {}  # Stores the last seen index of each card
    min_length = float("inf")  # Initialize min length to a large number

    for i, card in enumerate(cards):
        if card in last_seen:
            min_length = min(min_length, i - last_seen[card] + 1)  # Calculate subarray length
        last_seen[card] = i  # Update last seen index

    return min_length if min_length != float("inf") else -1  # Return -1 if no duplicate found

# Example Usage:
cards = [3, 4, 2, 3, 4, 7]
print(minimumCardPickup(cards))  # Output: 4
