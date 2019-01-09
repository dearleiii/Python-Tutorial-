class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot): 
            nums[right], nums[pivot] = nums[pivot], nums[right]
            store = left
            
            for i in range(left, right): 
                if nums[i] < nums[right]:
                    nums[i], nums[store] = nums[store], nums[i]
                    store += 1
            nums[store], nums[right] = nums[right], nums[store]
            
            return store
            
        
        def sort(left, right, k_smallest):
            if left == right: return nums[left]
        
            pivot = random.randint(left, right)
            pivot = partition(left, right, pivot)
            
            # pivot partitions left and right parts 
            if pivot == k_smallest:
                return nums[pivot]
            elif pivot < k_smallest:
                return sort(left, pivot - 1, k_smallest)
            else: 
                return sort(pivot + 1, right, k_smallest)
        
        return sort(0, len(nums) - 1, len(nums) - k)
