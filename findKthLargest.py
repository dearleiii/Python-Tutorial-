class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to the end 
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            
            # 2. move all smaller elements to the left 
            store_index = left 
            for i in range(left, right):
                if nums[i] < pivot: 
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
        
            # 3. move pivot to its final place 
            nums[right], nums[store_index] = nums[store_index], nums[right]
            
            return store_index
            
        def select(left, right, k_smallest): 
            # return the smallest element (left, right)
            if left == right:
                return nums[left]
            
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            
            # pivot is in its final position 
            if k_smallest == pivot_index: 
                return nums[k_smallest]
            elif k_smallest < pivot_index: 
                return select(left, pivot_index - 1, k_smallest)
            else: 
                return select(pivot_index + 1, right, k_smallest)
            
        return select(0, len(nums) - 1, len(nums) - k)
