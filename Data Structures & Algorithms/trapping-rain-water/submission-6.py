class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        highest_left = {}
        highest = 0
        for i in range(len(height)):
            if height[i] > highest:
                highest = height[i]

            highest_left[i] = highest

        highest_right = {}
        highest = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] > highest:
                highest = height[i]
            highest_right[i] = highest

        for i in range(len(height)):
            temp = min(highest_left[i], highest_right[i]) - height[i]
            if temp > 0:
                water += temp

        return water