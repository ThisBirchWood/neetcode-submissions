class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, n * m - 1

        while l <= r:
            mid = (l + r) // 2
            y = mid // m
            x = mid % m

            if matrix[y][x] > target:
                r = mid - 1
            elif matrix[y][x] < target:
                l = mid + 1
            else:
                return True

        return False          
            