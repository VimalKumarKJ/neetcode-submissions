import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        result = 0

        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while (len(stones) >= 2):
            y = - heapq.heappop(stones)
            x = - heapq.heappop(stones)

            if x < y:
                val = y - x
                heapq.heappush(stones, -val)
                result = val
            elif x == y:
                result = 0
        if len(stones) == 1:
            return -stones[0]
        return result
        