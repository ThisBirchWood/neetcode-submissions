class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        stack = []

        l_smaller = [-1] * n
        r_smaller = [-1] * n

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                r_smaller[j] = i
            stack.append(i)
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                l_smaller[j] = i
            stack.append(i)

        for i in range(n):
            l = l_smaller[i]
            r = r_smaller[i] if r_smaller[i] != -1 else n

            res = max(res, ((r - l - 1) * heights[i]))

        return res


        