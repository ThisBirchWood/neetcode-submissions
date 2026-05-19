class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        for i in range(len(height)):
            l_highest = 0
            for j in range(i, -1, -1):
                if height[j] > l_highest:
                    l_highest = height[j]

            r_highest = 0
            for j in range(i+1, len(height)):
                if height[j] > r_highest:
                    r_highest = height[j]

            temp = min(l_highest, r_highest) - height[i]
            if temp > 0:
                water += temp

        return water