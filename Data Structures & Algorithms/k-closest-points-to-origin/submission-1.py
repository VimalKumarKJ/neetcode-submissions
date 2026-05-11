import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        result = []
        def compute_distance(points):
            for i in range(n):
                x = points[i]
                y = [0,0]

                calc = sum((x[px] - y[px])**2 for px in range(len(x)))
                distance = math.sqrt(calc)

                points[i] = (distance, x)
            
            return points
        
        points = compute_distance(points)
        heapq.heapify(points)

        while(k>0):
            result.append(heapq.heappop(points)[1])
            k-=1
        return result