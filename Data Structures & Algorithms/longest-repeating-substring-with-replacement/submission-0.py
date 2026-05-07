class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        count, maxf = {}, 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxf = max(count[s[right]], maxf)
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res

            
            
                