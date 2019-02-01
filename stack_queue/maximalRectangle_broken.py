class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix is None or len(matrix) == 0: return 0
        if matrix[0] is None or len(matrix[0]) == 0: return 0
        
        area = 0
        for idx_row, row in enumerate(matrix): 
            matrix[idx_row] = matrix[idx_row] + ['0']
            for idx_col, elem in enumerate(matrix[idx_row]): 
                height = ord(elem) - ord('0')
                if idx_row == 0: 
                    # original number 
                    matrix[0][idx_col] = height
                else: 
                    # accumulate number 
                    if height == 0: 
                        matrix[idx_row][idx_col] = 0
                    else: 
                        matrix[idx_row][idx_col] = matrix[idx_row - 1][idx_col] + 1
              
        for idx_row, row in enumerate(matrix): 
            print(row)
            index_stack = []
            for idx_col, elem in enumerate(row): 
                while index_stack and row[index_stack[-1]] > height: 
                    # pop all 
                    popped_index = index_stack.pop()
                    left = index_stack[-1] if index_stack else -1
                    width = idx_col - left - 1
                    area = max(area, width * row[popped_index])
                    print(row[popped_index], width, area)
                
                index_stack.append(idx_col)
        
        return area
        
