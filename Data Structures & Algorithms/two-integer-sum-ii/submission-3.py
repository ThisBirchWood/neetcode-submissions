class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            c_sum = numbers[l] + numbers[r]

            if c_sum > target:
                r -= 1
            elif c_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
