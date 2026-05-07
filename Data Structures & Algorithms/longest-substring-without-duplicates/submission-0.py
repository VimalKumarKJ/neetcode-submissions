class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            temp = set()
            for j in range(i, len(s)):
                if s[j] in temp:
                    break
                temp.add(s[j])
            result = max(result, len(temp))
        return result
            