class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            next_higher = 0
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    next_higher = j - i
                    break

            res.append(next_higher)

        return res


