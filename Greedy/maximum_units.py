class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort the box types in decreasing order of units per box
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        total_units = 0
        boxes_loaded = 0
        
        # Iterate through the sorted box types
        for numberOfBoxes, unitsPerBox in boxTypes:
            if boxes_loaded + numberOfBoxes <= truckSize:
                # If we can fit all the boxes of this type, take all of them
                total_units += numberOfBoxes * unitsPerBox
                boxes_loaded += numberOfBoxes
            else:
                # Take as many boxes as we can fit
                remaining_boxes = truckSize - boxes_loaded
                total_units += remaining_boxes * unitsPerBox
                break
                
        return total_units

# Time Complexity: 
#    - Sorting the boxTypes array takes O(n log n), where n is the number of box types.
#    - After sorting, we iterate through the list once, which takes O(n).
#    - Thus, the total time complexity is O(n log n).
# Space Complexity:
#    - O(1) if we consider the input array as constant space (since the sorting operation modifies the array in-place).
 
