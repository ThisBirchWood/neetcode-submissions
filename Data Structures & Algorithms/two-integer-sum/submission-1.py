class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)):
            tar = target-nums[i]
            if tar in d and d[tar] != i:
                return [i, d[target-nums[i]]]

            