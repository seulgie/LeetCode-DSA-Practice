class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Find the next greater element for each element in nums1 based on nums2.

        Time Complexity:
        - O(n + m): Where n is the length of nums2 and m is the length of nums1.
          - O(n): To preprocess nums2 using a monotonic stack.
          - O(m): To build the result for nums1 using the dictionary.

        Space Complexity:
        - O(n): To store the mapping of elements in nums2 to their next greater elements.

        :param nums1: List[int] - Subset of nums2
        :param nums2: List[int] - Base array
        :return: List[int] - Next greater elements for nums1
        """
        next_greater = {}
        stack = []

        # Process nums2 to find next greater elements
        for num in nums2:
            # While stack is not empty and the top of the stack is smaller than the current number
            while stack and stack[-1] < num:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)

        # For remaining elements in the stack, there is no greater element
        while stack:
            next_greater[stack.pop()] = -1

        # Build the result for nums1 using the precomputed map
        return [next_greater[num] for num in nums1]
