class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        vals = {}

        for i, number in enumerate(numbers):
            vals[number] = i

        for i, number in enumerate(numbers):
            goal = target - number
            if goal in vals and vals[goal] > i:
                return [i+1, vals[goal]+1]

        return None
