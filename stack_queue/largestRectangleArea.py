class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if heights is None or len(heights) == 0: return 0
        indices_stack = []
        
        area = 0
        for index, height in enumerate(heights + [0]): 
            while indices_stack and heights[indices_stack[-1]] >= height: 
                popped_index = indices_stack.pop()
                left_index = indices_stack[-1] if indices_stack else -1
                width = index - left_index - 1
                area = max(area, width * heights[popped_index])
            
            indices_stack.append(index)
        return area
