class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Simplifies a Unix-style absolute path to its canonical form.
        
        :param path: str - The input absolute path
        :return: str - The simplified canonical path
        
        Time Complexity: O(n), where n is the length of the path string.
        Space Complexity: O(n) for the stack.
        """
        # Step 1: Split the path by slashes
        components = path.split('/')
        
        # Step 2: Use a stack to process the path components
        stack = []
        
        for component in components:
            if component == '' or component == '.':
                # Ignore empty components or single periods
                continue
            elif component == '..':
                # Pop the stack to go to the parent directory, if possible
                if stack:
                    stack.pop()
                    
            else:
                # Push valid directory names onto the stack
                stack.append(component)
                
        # Step 3: Reconstruct the canocical path
        return '/' + '/'.join(stack)
