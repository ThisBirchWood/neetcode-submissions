class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = {}
        out = []

        for i in range(len(numbers)):
            num = numbers[i]
            n[num] = i

        for i in range(len(numbers)):
            num = numbers[i]
            if target - num in n and n[target-num] != i:
                return [i+1, n[target-num]+1]
            