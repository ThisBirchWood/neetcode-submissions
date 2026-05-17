class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = len(position)
        ucars = []
        timesteps = {}

        for i in range(fleets):
            ucars.append((position[i], speed[i]))

        cars = sorted(ucars, key = lambda x: x[0], reverse=True)

        for i in range(len(cars)):
            car = cars[i]
            timesteps[i] = (target - car[0]) / car[1]

            if i > 0:
                if timesteps[i-1] >= timesteps[i]:
                    fleets -= 1
                    timesteps[i] = timesteps[i-1]

        return fleets
        


        




