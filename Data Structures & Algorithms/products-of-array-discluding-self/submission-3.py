class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        num_zeros = 0
        full = 1

        for num in nums:
            if num == 0:
                num_zeros += 1
            else:
                full *= num

        for num in nums:
            if num_zeros == 1 and num == 0:
                out.append(full)
                continue
            
            if num_zeros > 0:
                out.append(0)
                continue

            if num_zeros == 0:
                out.append(int(full/num))

            
        return out