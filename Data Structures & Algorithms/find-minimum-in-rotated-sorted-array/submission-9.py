class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_val = nums[0]

        while l <= r:
            mid = (l + r) // 2

            if nums[l] < nums[r]:
                return min(nums[l], min_val)

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
            
            min_val = min(nums[mid], min_val)

        return min_val

