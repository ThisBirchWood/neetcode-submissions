class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         duplicates = {}
         for num in nums:
            if num in duplicates:
                return True
            duplicates[num] = True

         return False