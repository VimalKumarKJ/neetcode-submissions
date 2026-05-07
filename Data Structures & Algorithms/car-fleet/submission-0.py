class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars = sorted(cars, reverse=True)

        for pos, speed in cars:
            req_time = (target-pos)/speed
            if not stack or  req_time > stack[-1]:
                stack.append(req_time)
        return len(stack)

