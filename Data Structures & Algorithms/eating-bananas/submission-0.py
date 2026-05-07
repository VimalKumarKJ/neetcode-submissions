class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = 0

        def calculate_hours(speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/speed)
            return hours

        
        while(left <= right):
            mid = left + (right - left) // 2
            total_hours = calculate_hours(mid)

            if total_hours > h:
                left = mid + 1
            else:
                result = mid
                right = mid - 1
        return result