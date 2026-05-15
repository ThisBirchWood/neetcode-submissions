class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = {}
        out = set()

        for i in range(len(nums)):
            num = nums[i]
            n[num] = i

        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(len(nums)):
                num2 = nums[j]

                target = -(num1 + num2)
                if target in n:
                    k = n[target]
                    if i != j and j != k and i != k:
                        output = tuple(sorted([num1, num2, target]))
                        out.add(output)

        return list(out)
