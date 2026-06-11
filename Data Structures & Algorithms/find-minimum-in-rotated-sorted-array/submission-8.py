class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_val = nums[0]

        while l <= r:
            m = (l + r) // 2

            if nums[l] < nums[r]:
                return min(min_val, nums[l])

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
            
            min_val = min(min_val, nums[m])
        
        return min_val
