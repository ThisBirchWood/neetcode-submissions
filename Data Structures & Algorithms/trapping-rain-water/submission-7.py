class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        highest_left = []
        highest = 0
        for i in range(len(height)):
            highest = max(highest, height[i])
            highest_left.append(highest)

        highest_right = []
        highest = 0
        for i in range(len(height)-1, -1, -1):
            highest = max(highest, height[i])
            highest_right.append(highest)


        for i in range(len(height)):
            temp = min(highest_left[i], highest_right[len(height) - 1 - i]) - height[i]
            if temp > 0:
                water += temp

        return water